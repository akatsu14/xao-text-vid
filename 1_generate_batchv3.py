import os
from pathlib import Path

# ==================================================
# ====== KHAI BÁO PHẲNG – SỬA TẠI ĐÂY ======
# ==================================================

# Thư mục raw source (mirror folder)
# Ví dụ: input/job1/a.txt
INPUT_DIR = "input"

# Nơi lưu FULL PROMPT đã ghép (mirror folder)
# Ví dụ: specific_template/job1/a_fullprompt.txt
SPECIFIC_TEMPLATE_DIR = "specific_template"

# Master prompt template (PHẢI có {raw_input_data}
# KHUYẾN NGHỊ: dùng bản v3 có thêm {specific_instructions}
MASTER_PROMPT_FILE = "M_prompt3.txt"

# Log để không build lại
LOG_DIR = "logs"
LOG_FILE = "built_full_prompts.log"

ENCODING = "utf-8"

# Quy ước tên file output
# input/job1/a.txt → specific_template/job1/a_fullprompt.txt
OUTPUT_SUFFIX = "_fullprompt.txt"

# Nếu True: nếu fullprompt đã tồn tại thì skip
SKIP_IF_EXISTS = True

# Marker để người dùng điền yêu cầu cụ thể
BEGIN_SPECIFIC_INSTRUCTIONS = "<<<BEGIN_SPECIFIC_INSTRUCTIONS>>>"
END_SPECIFIC_INSTRUCTIONS   = "<<<END_SPECIFIC_INSTRUCTIONS>>>"

# ==================================================
# ================== UTILS =========================
# ==================================================

def read_text(p: Path) -> str:
    return p.read_text(encoding=ENCODING)

def write_text(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding=ENCODING)

def load_log(p: Path) -> set:
    if not p.exists():
        return set()
    return set(
        line.strip()
        for line in p.read_text(encoding=ENCODING).splitlines()
        if line.strip()
    )

def append_log(p: Path, key: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding=ENCODING) as f:
        f.write(key + "\n")

def make_key(input_root: Path, raw_path: Path) -> str:
    # Key theo path tương đối, không extension
    # VD: job1/a
    rel = raw_path.relative_to(input_root)
    return rel.with_suffix("").as_posix()

def build_instruction_skeleton(raw_rel_path: Path) -> str:
    return (
        f"{BEGIN_SPECIFIC_INSTRUCTIONS}\n"
        f"# Article: {raw_rel_path.as_posix()}\n"
        f"# Điền yêu cầu cụ thể cho bài này (KHÔNG dán raw source vào đây)\n\n"
        f"- Target audience:\n"
        f"- Primary angle / thesis:\n"
        f"- Must-include points (3–8 bullets max):\n"
        f"- Keywords / entities to emphasize:\n"
        f"- Things to avoid / do-not-claim:\n"
        f"- Output constraints (optional):\n\n"
        f"{END_SPECIFIC_INSTRUCTIONS}"
    )

def build_full_prompt(master: str, raw_source: str, instruction_block: str) -> str:
    if "{raw_input_data}" not in master:
        raise RuntimeError("❌ Master prompt thiếu placeholder {raw_input_data}")

    raw_source = raw_source.strip()

    # Trường hợp master có slot riêng cho instructions (chuẩn nhất)
    if "{specific_instructions}" in master:
        return (
            master
            .replace("{specific_instructions}", instruction_block)
            .replace("{raw_input_data}", raw_source)
        )

    # Fallback: master cũ – chèn instructions TRƯỚC RAW SOURCE
    insert_block = (
        "\n\nARTICLE-SPECIFIC INSTRUCTIONS (ONLY FOR THIS ARTICLE):\n"
        f"{instruction_block}\n"
    )

    idx = master.find("\n4. RAW SOURCE DATA:")
    if idx != -1:
        master2 = master[:idx] + insert_block + master[idx:]
        return master2.replace("{raw_input_data}", raw_source)

    # Fallback cuối: prepend
    return (insert_block + "\n" + master).replace("{raw_input_data}", raw_source)

# ==================================================
# ================== MAIN ==========================
# ==================================================

def main():
    input_root = Path(INPUT_DIR)
    spec_root = Path(SPECIFIC_TEMPLATE_DIR)
    master_path = Path(MASTER_PROMPT_FILE)
    log_path = Path(LOG_DIR) / LOG_FILE

    if not input_root.exists():
        print(f"❌ INPUT_DIR không tồn tại: {input_root.resolve()}")
        return

    if not master_path.exists():
        print(f"❌ MASTER_PROMPT_FILE không tồn tại: {master_path.resolve()}")
        return

    master = read_text(master_path)

    raw_files = sorted(p for p in input_root.rglob("*.txt") if p.is_file())
    if not raw_files:
        print("❌ Không tìm thấy file .txt trong input/")
        return

    done = load_log(log_path)

    created = skipped = existed = failed = 0

    for raw_path in raw_files:
        key = make_key(input_root, raw_path)
        rel = raw_path.relative_to(input_root)

        out_path = spec_root / rel.parent / f"{rel.stem}{OUTPUT_SUFFIX}"

        if key in done:
            skipped += 1
            continue

        if SKIP_IF_EXISTS and out_path.exists():
            existed += 1
            append_log(log_path, key)
            continue

        try:
            raw_source = read_text(raw_path)
            instruction_block = build_instruction_skeleton(rel)
            full_prompt = build_full_prompt(master, raw_source, instruction_block)

            write_text(out_path, full_prompt)
            append_log(log_path, key)
            created += 1

            print(f"[FULLPROMPT] {key} → {out_path.as_posix()}")
        except Exception as e:
            failed += 1
            print(f"[ERROR] {key}: {e}")

    print("--------------------------------------------------")
    print(f"✅ Done | created={created}, skipped={skipped}, existed={existed}, failed={failed}")
    print(f"Log: {log_path.resolve()}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()