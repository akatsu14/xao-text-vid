import re
import sys
import time
import random
import subprocess
import os
import shutil
import importlib.util
import html
import json
from pathlib import Path
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urlparse, parse_qs

# Avoid UnicodeEncodeError for the Vietnamese/emoji status messages when output
# is redirected or CMD is using a legacy code page.
for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="replace")

# ========= CONFIG =========
SCRIPT_DIR = Path(__file__).resolve().parent

INPUT_FILE = SCRIPT_DIR / "Youtube Links.txt"

OUTPUT_DIR = SCRIPT_DIR / "texts"      # ONLY .txt output
TMP_DIR = SCRIPT_DIR / "subs_tmp"      # temp captions
FAILED_LOG_PATH = SCRIPT_DIR / "failed_links.txt"

# Resume logs
SUCCESS_LOG_PATH = SCRIPT_DIR / "success_links.txt"          # append-only: vid \t url \t outname
MISSING_OUTPUT_LOG_PATH = SCRIPT_DIR / "missing_output.txt"  # urls in success log but missing output file

# Cookies priority: cookies.txt next to this script (Netscape format)
COOKIES_FILE = Path(__file__).resolve().with_name("cookies.txt")
CHROME_COOKIES_SPEC = "chrome"  # fallback only if cookies.txt missing

# Retry
MAX_ATTEMPTS = 6
BASE_SLEEP = 6  # exponential backoff per-attempt when 429

# Player clients to try
# "default" means "do NOT force player_client"
CLIENT_ROTATION = ["default", "web", "android", "tv", "web_safari"]

# Sleep policy between videos
NORMAL_SLEEP_RANGE = (1, 2)
PENALTY_SLEEP_RANGE = (5, 10)
PENALTY_VIDEOS_AFTER_429 = 5

INVALID_CHARS = r'[\\/*?:"<>|]'

# BALANCED then SAFE
SAFE_FROM_ATTEMPT = 3  # attempts 1-2 balanced, attempt 3+ safe
BALANCED_OPTS = [
    "--retries", "3",
    "--fragment-retries", "3",
    "--concurrent-fragments", "2",
]
SAFE_OPTS = [
    "--retries", "10",
    "--fragment-retries", "10",
    "--concurrent-fragments", "1",
    "--sleep-requests", "1",
]

# Filled by dependency preflight. Environment overrides accept either an
# executable path or a directory containing the executable.
YTDLP_CMD: List[str] = ["yt-dlp"]
FFMPEG_ARGS: List[str] = []
JS_RUNTIME_ARGS = ["--js-runtimes", "node"]
# If you don't want remote fetch, install `yt-dlp-ejs` and you can remove this.
REMOTE_COMPONENTS_ARGS = ["--remote-components", "ejs:github"]


# ----------------- dependency preflight -----------------
def resolve_executable(name: str, env_name: str) -> Optional[str]:
    raw = os.environ.get(env_name, "").strip().strip('"')
    if raw:
        p = Path(raw).expanduser()
        if p.is_dir():
            p = p / f"{name}.exe"
        if p.is_file():
            return str(p.resolve())

    found = shutil.which(name)
    if found:
        return str(Path(found).resolve())

    for folder in (SCRIPT_DIR / "tools", SCRIPT_DIR / "bin"):
        candidate = folder / f"{name}.exe"
        if candidate.is_file():
            return str(candidate.resolve())
    return None


def preflight_dependencies() -> bool:
    global YTDLP_CMD, FFMPEG_ARGS, JS_RUNTIME_ARGS

    problems: List[str] = []

    yt_dlp_exe = resolve_executable("yt-dlp", "YTDLP_PATH")
    if yt_dlp_exe:
        YTDLP_CMD = [yt_dlp_exe]
    elif importlib.util.find_spec("yt_dlp") is not None:
        YTDLP_CMD = [sys.executable, "-m", "yt_dlp"]
    else:
        problems.append(
            "yt-dlp chưa được cài cho Python đang chạy. Cài bằng: "
            f'"{sys.executable}" -m pip install -U "yt-dlp[default]" youtube-transcript-api'
        )

    node_exe = resolve_executable("node", "NODE_PATH")
    if node_exe:
        JS_RUNTIME_ARGS = ["--js-runtimes", f"node:{node_exe}"]
        rc, out, err = run_cmd([node_exe, "--version"])
        m = re.search(r"v?(\d+)", out or err)
        if rc != 0 or not m:
            problems.append(f"Không chạy được Node.js tại: {node_exe}")
        elif int(m.group(1)) < 22:
            problems.append(f"Node.js {out or err} quá cũ; yt-dlp hiện cần Node.js 22 trở lên.")
    else:
        problems.append(
            "Không tìm thấy Node.js. Hãy cài Node.js 22+ hoặc đặt biến NODE_PATH "
            "trỏ tới node.exe."
        )

    ffmpeg_exe = resolve_executable("ffmpeg", "FFMPEG_PATH")
    if ffmpeg_exe:
        FFMPEG_ARGS = ["--ffmpeg-location", ffmpeg_exe]
    else:
        problems.append(
            "Không tìm thấy ffmpeg.exe. Script cần FFmpeg để chạy --convert-subs vtt. "
            "Hãy thêm FFmpeg vào PATH hoặc đặt biến FFMPEG_PATH."
        )

    if problems:
        print("❌ Thiếu dependency hoặc PATH chưa đúng:")
        for item in problems:
            print(f"  - {item}")
        print(f"  - Python đang chạy: {sys.executable}")
        return False

    print(f"✅ yt-dlp: {' '.join(YTDLP_CMD)}")
    print(f"✅ Node.js: {node_exe}")
    print(f"✅ FFmpeg: {ffmpeg_exe}")
    return True


# ----------------- cookies args -----------------
def add_cookies_args(cmd: List[str]) -> List[str]:
    """
    Priority:
      1) cookies.txt (Netscape) next to script (stable; Chrome can stay open)
      2) live Chrome cookies (fallback if cookies.txt missing)
    """
    if COOKIES_FILE.exists() and COOKIES_FILE.is_file():
        return cmd[:len(YTDLP_CMD)] + ["--cookies", str(COOKIES_FILE)] + cmd[len(YTDLP_CMD):]
    return cmd[:len(YTDLP_CMD)] + ["--cookies-from-browser", CHROME_COOKIES_SPEC] + cmd[len(YTDLP_CMD):]


# ----------------- error detectors -----------------
def is_429(msg: str) -> bool:
    m = (msg or "").lower()
    return ("http error 429" in m) or ("too many requests" in m) or (re.search(r"\b429\b", m) is not None)

def is_403(msg: str) -> bool:
    m = (msg or "").lower()
    return ("http error 403" in m) or ("403: forbidden" in m) or (re.search(r"\b403\b", m) is not None)

def is_format_unavailable(msg: str) -> bool:
    m = (msg or "").lower()
    return ("requested format is not available" in m) or ("format is not available" in m)

def is_fragment_error(msg: str) -> bool:
    m = (msg or "").lower()
    return ("fragment" in m and "not found" in m) or ("unable to continue" in m)

def is_cookie_db_error(msg: str) -> bool:
    m = (msg or "").lower()
    return "could not copy chrome cookie database" in m

def is_cookie_invalid_or_bot(msg: str) -> bool:
    m = (msg or "").lower()
    return (
        "cookies are no longer valid" in m
        or "login_required" in m
        or "sign in to confirm you’re not a bot" in m
        or "sign in to confirm you're not a bot" in m
        or "confirm you’re not a bot" in m
        or "confirm you're not a bot" in m
    )

def is_cookie_format_error(msg: str) -> bool:
    m = (msg or "").lower()
    return "cookies file must be netscape formatted" in m

def is_ejs_challenge_failed(msg: str) -> bool:
    m = (msg or "").lower()
    return ("n challenge solving failed" in m) or ("youtube extraction without a js runtime" in m)


# ----------------- helpers -----------------
def sanitize_filename(name: str) -> str:
    name = re.sub(INVALID_CHARS, "", name).strip()
    return name or "untitled"

def read_links(path: Path) -> List[str]:
    if not path.exists():
        print(f"❌ Không thấy file: {path}")
        sys.exit(1)
    links = [ln.strip() for ln in path.read_text(encoding="utf-8", errors="ignore").splitlines() if ln.strip()]
    seen, out = set(), []
    for u in links:
        if u not in seen:
            out.append(u)
            seen.add(u)
    return out

def extract_vid(url: str) -> str:
    u = url.strip()
    pr = urlparse(u)

    if pr.netloc.endswith("youtu.be"):
        return pr.path.strip("/").split("/")[0]

    qs = parse_qs(pr.query)
    if "v" in qs and qs["v"]:
        return qs["v"][0]

    parts = [p for p in pr.path.split("/") if p]
    for i, p in enumerate(parts):
        if p in ("shorts", "live") and i + 1 < len(parts):
            return parts[i + 1]

    return parts[-1] if parts else u

def run_cmd(cmd: List[str]) -> Tuple[int, str, str]:
    try:
        p = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            cwd=SCRIPT_DIR,
        )
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except FileNotFoundError as exc:
        return 127, "", f"Không tìm thấy chương trình: {exc.filename}"
    except OSError as exc:
        return 126, "", f"Không chạy được lệnh {cmd[0]}: {exc}"

def append_line(path: Path, line: str):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")

def cleanup_vid_tmp(vid: str):
    if not TMP_DIR.exists():
        return
    for p in TMP_DIR.glob(f"{vid}.*"):
        try:
            p.unlink()
        except Exception:
            pass


# ----------------- resume indexes -----------------
def load_success_indexes() -> Tuple[Dict[str, Tuple[str, str]], Dict[str, Tuple[str, str]]]:
    """
    Returns:
      by_url[url] = (vid, outname)
      by_vid[vid] = (url, outname)
    """
    by_url: Dict[str, Tuple[str, str]] = {}
    by_vid: Dict[str, Tuple[str, str]] = {}
    if not SUCCESS_LOG_PATH.exists():
        return by_url, by_vid

    for ln in SUCCESS_LOG_PATH.read_text(encoding="utf-8", errors="ignore").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        parts = ln.split("\t")
        vid = parts[0].strip() if len(parts) > 0 else ""
        url = parts[1].strip() if len(parts) > 1 else ""
        outname = parts[2].strip() if len(parts) > 2 else ""
        if url:
            by_url[url] = (vid, outname)
        if vid:
            by_vid[vid] = (url, outname)
    return by_url, by_vid

def output_file_exists_for_vid(vid: str) -> bool:
    if not OUTPUT_DIR.exists():
        return False
    for p in OUTPUT_DIR.glob(f"* [{vid}].txt"):
        if p.is_file():
            return True
    return False

def log_success(vid: str, url: str, out_name: str):
    append_line(SUCCESS_LOG_PATH, f"{vid}\t{url}\t{out_name}")


# ----------------- caption cleaning -----------------
def dedupe_lines(lines: List[str]) -> List[str]:
    """
    Balanced: remove immediate duplicates strongly,
    and window-dedupe for very short lines.
    """
    out: List[str] = []
    recent: List[str] = []
    window = 6

    for raw in lines:
        t = raw.strip()
        if not t:
            continue

        norm = re.sub(r"\s+", " ", t).strip().lower()

        if out:
            prev_norm = re.sub(r"\s+", " ", out[-1]).strip().lower()
            if norm == prev_norm:
                continue

        if len(norm.split()) <= 3:
            if norm in recent:
                continue

        out.append(t)

        recent.append(norm)
        if len(recent) > window:
            recent.pop(0)

    return out

def caption_file_to_text(p: Path) -> str:
    raw_lines: List[str] = []
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            t = line.strip()
            if not t:
                continue
            if t.isdigit():
                continue
            if "-->" in t:
                continue
            if t.startswith("WEBVTT"):
                continue
            if t.startswith("Kind:") or t.startswith("Language:"):
                continue

            t = re.sub(r"<[^>]+>", "", t)
            t = html.unescape(t)
            t = t.replace("\u200b", "").strip()
            if not t:
                continue
            raw_lines.append(t)

    cleaned = dedupe_lines(raw_lines)
    text = "\n".join(cleaned)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


# ----------------- IO -----------------
def save_txt(title: str, vid: str, text: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    safe_title = sanitize_filename(title)
    out_path = OUTPUT_DIR / f"{safe_title} [{vid}].txt"
    out_path.write_text(f"{title}\n\n{text.strip()}", encoding="utf-8")
    return out_path


# ----------------- yt-dlp: info (single json) -----------------
def yt_dlp_dump_info(url: str, client: str) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    cmd = [
        *YTDLP_CMD,
        "--skip-download",
        "--no-warnings",
        "--no-progress",
        "--dump-single-json",
        *JS_RUNTIME_ARGS,
        *REMOTE_COMPONENTS_ARGS,
        *FFMPEG_ARGS,
        url,
    ]

    if client != "default":
        cmd += ["--extractor-args", f"youtube:player_client={client}"]

    cmd = add_cookies_args(cmd)

    rc, out, err = run_cmd(cmd)
    if rc != 0:
        return False, (err or out or f"yt-dlp dump json exit code {rc}"), None

    try:
        info = json.loads(out)
        return True, "OK", info
    except Exception:
        return False, "Failed to parse JSON from yt-dlp output", None

def choose_best_sub_lang(info: Dict[str, Any]) -> Tuple[Optional[str], bool]:
    """
    Returns (lang_code, is_auto)
    Preference:
      1) manual subs in original language if available
      2) any manual subs
      3) auto captions in original language
      4) any auto captions
    """
    orig_lang = (info.get("language") or "").strip()
    subs: Dict[str, Any] = info.get("subtitles") or {}
    autos: Dict[str, Any] = info.get("automatic_captions") or {}

    def pick_lang_from(d: Dict[str, Any], prefer: str) -> Optional[str]:
        if prefer and prefer in d:
            return prefer
        if prefer:
            for k in d.keys():
                if k.lower().startswith(prefer.lower() + "-"):
                    return k
        keys = sorted(d.keys())
        return keys[0] if keys else None

    lang = pick_lang_from(subs, orig_lang)
    if lang:
        return lang, False

    lang = pick_lang_from(autos, orig_lang)
    if lang:
        return lang, True

    return None, False


# ----------------- yt-dlp: download selected subtitle -----------------
def yt_dlp_download_sub(url: str, client: str, lang: str, safe: bool) -> Tuple[bool, str]:
    """
    IMPORTANT:
      - Use '--sub-format best' to accept available subtitle formats (srv3/ttml/etc)
      - Convert to vtt so our parser works consistently.
    Requires ffmpeg in PATH.
    """
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    vid = extract_vid(url)
    cleanup_vid_tmp(vid)

    cmd = [
        *YTDLP_CMD,
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", lang,
        "--sub-format", "best",
        "--convert-subs", "vtt",
        "--no-warnings",
        "--no-progress",
        "--extractor-retries", "3",
        "--geo-bypass",
        *JS_RUNTIME_ARGS,
        *REMOTE_COMPONENTS_ARGS,
        *FFMPEG_ARGS,
        "-o", str(TMP_DIR / "%(id)s"),
        url,
    ]

    if client != "default":
        cmd += ["--extractor-args", f"youtube:player_client={client}"]

    cmd += (SAFE_OPTS if safe else BALANCED_OPTS)
    cmd = add_cookies_args(cmd)

    rc, out, err = run_cmd(cmd)
    if rc == 0:
        return True, out
    return False, (err or out or f"yt-dlp exit code {rc}")

def pick_caption_file(vid: str, lang: str) -> Optional[Path]:
    if not TMP_DIR.exists():
        return None

    patterns = [
        f"{vid}.{lang}*.vtt",
        f"{vid}.*.vtt",
        f"{vid}.{lang}*.srt",
        f"{vid}.*.srt",
    ]

    cands: List[Path] = []
    for pat in patterns:
        cands.extend(list(TMP_DIR.glob(pat)))

    if not cands:
        return None

    def score(p: Path) -> int:
        n = p.name.lower()
        s = 100
        if n.endswith(".vtt"):
            s -= 20
        if f".{lang.lower()}" in n:
            s -= 20
        if "asr" in n or "auto" in n:
            s += 5
        if "orig" in n:
            s += 1
        return s

    cands.sort(key=score)
    return cands[0]


# ----------------- API fallback -----------------
def api_fallback_any(url: str) -> Optional[str]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except Exception:
        return None

    vid = extract_vid(url)
    try:
        tr_list = YouTubeTranscriptApi.list_transcripts(vid)

        chosen = None
        for t in tr_list:
            is_generated = getattr(t, "is_generated", None)
            if is_generated is False:
                chosen = t
                break
            if chosen is None:
                chosen = t

        if chosen is None:
            return None

        segs = chosen.fetch()
        txt = "\n".join(s.get("text", "") for s in segs if s.get("text"))
        return txt.strip() or None
    except Exception:
        return None


# ----------------- per-video pipeline -----------------
def download_one(url: str) -> Tuple[bool, str, bool]:
    vid = extract_vid(url)
    last_reason = ""
    hit_429 = False
    force_safe = False
    title = vid

    for attempt in range(1, MAX_ATTEMPTS + 1):
        client = CLIENT_ROTATION[(attempt - 1) % len(CLIENT_ROTATION)]
        safe = force_safe or (attempt >= SAFE_FROM_ATTEMPT)
        mode = "SAFE" if safe else "BALANCED"
        print(f"  ▶ Attempt {attempt} (client={client}, mode={mode})")

        ok_info, info_msg, info = yt_dlp_dump_info(url, client)
        if not ok_info or not info:
            last_reason = info_msg

            if is_cookie_format_error(last_reason):
                return False, (
                    "❌ cookies.txt không đúng định dạng Netscape.\n"
                    "➡️ Hãy export cookies theo Netscape format (hoặc convert JSON -> Netscape) rồi chạy lại."
                ), hit_429

            if is_cookie_db_error(last_reason):
                return False, (
                    "❌ Could not copy Chrome cookie database.\n"
                    "➡️ Cách fix ổn định nhất: dùng cookies.txt (Netscape) đặt cạnh DownSub.py.\n"
                    "➡️ Hoặc đóng hết chrome.exe rồi chạy lại."
                ), hit_429

        else:
            title = (info.get("title") or vid).strip() or vid
            chosen_lang, is_auto = choose_best_sub_lang(info)

            if not chosen_lang:
                last_reason = "No subtitles / auto captions available (per yt-dlp info)"
            else:
                print(f"    📝 Picked subtitle: lang={chosen_lang} ({'auto' if is_auto else 'manual'})")
                ok_dl, msg = yt_dlp_download_sub(url, client, chosen_lang, safe=safe)
                if ok_dl:
                    cap_file = pick_caption_file(vid, chosen_lang)
                    if cap_file and cap_file.exists():
                        text = caption_file_to_text(cap_file)
                        if not text:
                            last_reason = "Caption parsed empty"
                        else:
                            out = save_txt(title, vid, text)
                            log_success(vid, url, out.name)
                            return True, f"✅ Saved: {out.name} (lang={chosen_lang})", hit_429
                    else:
                        last_reason = "yt-dlp ok but caption file not found"
                else:
                    last_reason = msg

        if is_cookie_invalid_or_bot(last_reason):
            print("⚠️  Detected login/bot/cookies issue. Nếu dùng cookies.txt: hãy export lại cookies mới.")

        if is_ejs_challenge_failed(last_reason):
            print("⚠️  EJS/JS challenge failed. Hãy chắc chắn node hoạt động và remote-components ejs đã được tải được.")

        if is_429(last_reason):
            hit_429 = True
            sleep_s = BASE_SLEEP * (2 ** (attempt - 1)) + random.uniform(0.5, 2.0)
            print(f"⏳ 429 -> backoff {sleep_s:.1f}s rồi thử lại...")
            time.sleep(sleep_s)
            continue

        if is_403(last_reason) or is_fragment_error(last_reason):
            force_safe = True
            pause = 3.5 + random.uniform(0.8, 2.0)
            print(f"⛔ 403/fragment -> bật SAFE từ attempt sau, nghỉ {pause:.1f}s...")
            time.sleep(pause)
            continue

        if is_format_unavailable(last_reason):
            pause = 2.0 + random.uniform(0.5, 1.5)
            print(f"⚠️ format unavailable -> thử client khác sau {pause:.1f}s")
            time.sleep(pause)
            continue

        pause = 1.8 + random.uniform(0.5, 1.5)
        print(f"⚠️  fail: {str(last_reason)[:160]}... -> retry after {pause:.1f}s")
        time.sleep(pause)

    print("↘️  Fallback youtube-transcript-api (any language)...")
    fb = api_fallback_any(url)
    if fb:
        out = save_txt(title, vid, fb)
        log_success(vid, url, out.name)
        return True, f"✅ (fallback) Saved: {out.name}", hit_429

    return False, f"❌ FAIL: {last_reason}", hit_429


def main():
    if not preflight_dependencies():
        sys.exit(2)

    links = read_links(INPUT_FILE)

    print(f"📍 CWD: {Path.cwd()}")
    print(f"📥 Tổng video: {len(links)}")
    print(f"📂 Output dir: {OUTPUT_DIR.resolve()}")
    print(f"🗂  Tmp dir: {TMP_DIR.resolve()}")

    if COOKIES_FILE.exists() and COOKIES_FILE.is_file():
        print(f"🍪 Cookies: {COOKIES_FILE} (priority)")
    else:
        print("🍪 Cookies: (no cookies.txt) -> fallback --cookies-from-browser chrome")

    print("🧠 JS runtime: --js-runtimes node")
    print("🧩 EJS remote components: --remote-components ejs:github")

    ok_cnt, fail_cnt, skip_cnt, redo_cnt = 0, 0, 0, 0
    failed_items: List[Tuple[str, str]] = []

    penalty_videos_remaining = 0
    success_by_url, _success_by_vid = load_success_indexes()

    for i, url in enumerate(links, 1):
        vid = extract_vid(url)
        print(f"\n=== [{i}/{len(links)}] {url}")
        print(f"🆔 Video ID: {vid}")

        if output_file_exists_for_vid(vid):
            print("⏭️  Skip: đã có output file (theo texts/* [vid].txt)")
            skip_cnt += 1
            continue

        if url in success_by_url:
            _vid, outname = success_by_url[url]
            if outname and (OUTPUT_DIR / outname).exists():
                print("⏭️  Skip: đã có trong success log và output file còn tồn tại")
                skip_cnt += 1
                continue
            else:
                print("♻️  In success log but output missing -> reprocess")
                append_line(MISSING_OUTPUT_LOG_PATH, url)
                redo_cnt += 1

        success, info, hit_429 = download_one(url)
        print(info)

        if success:
            ok_cnt += 1
        else:
            fail_cnt += 1
            failed_items.append((url, info))

        if hit_429:
            penalty_videos_remaining = PENALTY_VIDEOS_AFTER_429

        sleep_range = PENALTY_SLEEP_RANGE if penalty_videos_remaining > 0 else NORMAL_SLEEP_RANGE
        if penalty_videos_remaining > 0:
            penalty_videos_remaining -= 1

        pause = random.uniform(*sleep_range)
        print(f"🕒 Nghỉ {pause:.1f}s (range={sleep_range[0]}–{sleep_range[1]}s)")
        time.sleep(pause)

    print("\n====================")
    print(f"OK={ok_cnt} | FAIL={fail_cnt} | SKIP={skip_cnt} | REDO={redo_cnt}")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"Success log: {SUCCESS_LOG_PATH.resolve()}")
    if MISSING_OUTPUT_LOG_PATH.exists():
        print(f"Missing-output log: {MISSING_OUTPUT_LOG_PATH.resolve()}")

    if failed_items:
        FAILED_LOG_PATH.write_text("\n".join([f"{u}\t{r}" for u, r in failed_items]), encoding="utf-8")
        print(f"📝 Fail log: {FAILED_LOG_PATH.resolve()}")


if __name__ == "__main__":
    main()
