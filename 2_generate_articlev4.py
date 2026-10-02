import os
import sys
import re
from pathlib import Path
import google.generativeai as genai

# ==================================================
# ====== KHAI BÁO PHẲNG – SỬA TẠI ĐÂY ======
# ==================================================

# Đọc PROMPT HOÀN CHỈNH đã build sẵn trong specific_template/**/_fullprompt.txt
SPECIFIC_TEMPLATE_DIR = "specific_template"

# Output mirror đúng cấu trúc folder theo specific_template
OUTPUT_DIR = "output"

# Log để không chạy lại
LOG_DIR = "logs"
DONE_LOG_FILE = "gemini_done.log"

# Gemini config
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-pro")
TEMPERATURE = 0.4
MAX_OUTPUT_TOKENS = 8192

ENCODING = "utf-8"

# Nếu True: đã có output file thì skip (dù log chưa có)
SKIP_IF_OUTPUT_EXISTS = False

# Pattern input full prompt
FULLPROMPT_SUFFIX = "_fullprompt.txt"   # do script build_fullprompts tạo ra
OUT_SUFFIX = "_out.txt"

# SEO word count warning (optional)
SEO_MIN_WORDS = 3500
SEO_MAX_WORDS = 3800

# ==================================================
# ================== UTILS =========================
# ==================================================

_word_re = re.compile(r"\b\w+(?:'\w+)?\b", re.UNICODE)

def count_words(text: str) -> int:
    return len(_word_re.findall(text or ""))

def read_text(p: Path) -> str:
    return p.read_text(encoding=ENCODING)

def write_text(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding=ENCODING)

def load_log(p: Path) -> set:
    if not p.exists():
        return set()
    return set(x.strip() for x in p.read_text(encoding=ENCODING).splitlines() if x.strip())

def append_log(p: Path, key: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding=ENCODING) as f:
        f.write(key + "\n")

def make_key_and_outpath(specific_root: Path, output_root: Path, fullprompt_path: Path) -> tuple[str, Path]:
    # key theo đường dẫn tương đối (không suffix _fullprompt)
    rel = fullprompt_path.relative_to(specific_root)  # job1/a_fullprompt.txt
    stem = rel.stem
    if stem.endswith("_fullprompt"):
        stem_base = stem[: -len("_fullprompt")]
    else:
        stem_base = stem
    key = (rel.parent / stem_base).as_posix()

    out_path = output_root / rel.parent / f"{stem_base}{OUT_SUFFIX}"
    return key, out_path

def gemini_generate(model: genai.GenerativeModel, prompt: str) -> str:
    resp = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "temperature": TEMPERATURE,
        },
    )
    return resp.text or ""

# ==================================================
# ================== MAIN ==========================
# ==================================================

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY chưa set")
        sys.exit(1)

    specific_root = Path(SPECIFIC_TEMPLATE_DIR)
    output_root = Path(OUTPUT_DIR)
    log_file = Path(LOG_DIR) / DONE_LOG_FILE

    if not specific_root.exists():
        print(f"❌ SPECIFIC_TEMPLATE_DIR không tồn tại: {specific_root.resolve()}")
        sys.exit(1)

    # Quét tất cả *_fullprompt.txt trong specific_template/ (bao gồm folder con)
    prompt_files = sorted([p for p in specific_root.rglob(f"*{FULLPROMPT_SUFFIX}") if p.is_file()])
    if not prompt_files:
        print(f"❌ Không có file *{FULLPROMPT_SUFFIX} trong: {specific_root.resolve()}")
        sys.exit(1)

    done = load_log(log_file)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(MODEL_NAME)

    processed = skipped = failed = 0

    for pf in prompt_files:
        key, out_path = make_key_and_outpath(specific_root, output_root, pf)

        if key in done:
            skipped += 1
            continue
        if SKIP_IF_OUTPUT_EXISTS and out_path.exists():
            skipped += 1
            continue

        try:
            full_prompt = read_text(pf)
        except Exception as e:
            failed += 1
            print(f"[ERROR] Read prompt failed: {key} | {pf} | {e}")
            continue

        if "{raw_input_data}" in full_prompt or "{specific_instructions}" in full_prompt:
            print(f"[WARN] {key} vẫn còn placeholder {{raw_input_data}}/{{specific_instructions}}. Hãy chạy tool build_fullprompts hoặc kiểm tra file: {pf.as_posix()}")

        print(f"\n[GEMINI] {key}")
        print(f"  prompt: {pf.as_posix()}")

        try:
            text = gemini_generate(model, full_prompt)
            wc = count_words(text)

            write_text(out_path, text)
            append_log(log_file, key)
            processed += 1

            print(f"[DONE] {key} | words={wc} | out={out_path.as_posix()}")
            if wc < SEO_MIN_WORDS or wc > SEO_MAX_WORDS:
                print(f"⚠️  WARNING: {key} lệch target ({SEO_MIN_WORDS}–{SEO_MAX_WORDS})")
        except Exception as e:
            failed += 1
            print(f"[ERROR] {key}: {e}")

    print("\n--------------------------------------------------")
    print(f"✅ Done | processed={processed}, skipped={skipped}, failed={failed}")
    print(f"Log: {log_file.resolve()}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
