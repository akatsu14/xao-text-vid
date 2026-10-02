import zipfile
import re
import hashlib
from pathlib import Path, PurePosixPath

ZIP_FILE = r"Input\20260818 The Royalist\done-20260819T081420Z-1-001.zip"
OUTPUT_DIR = r"quilbot\20260818 The Royalist"

MAX_PART_LENGTH = 60   # max length of each folder/file name
MAX_FULL_PATH = 240    # safe limit for Windows


def clean_name(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = name.strip().strip(".")
    return name or "unnamed"


def shorten_name(name: str, max_len: int = MAX_PART_LENGTH) -> str:
    name = clean_name(name)

    if len(name) <= max_len:
        return name

    path = PurePosixPath(name)
    suffix = path.suffix
    stem = path.stem

    hash_text = hashlib.md5(name.encode("utf-8")).hexdigest()[:8]
    keep_len = max_len - len(suffix) - len(hash_text) - 1

    if keep_len < 10:
        keep_len = max_len - len(hash_text) - 1
        return f"{name[:keep_len]}_{hash_text}"

    return f"{stem[:keep_len]}_{hash_text}{suffix}"


def safe_extract(zip_path, output_dir):
    zip_path = Path(zip_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        for item in zf.infolist():
            original_name = item.filename

            # Skip empty or unsafe paths
            parts = [
                shorten_name(part)
                for part in PurePosixPath(original_name).parts
                if part not in ("", ".", "..")
            ]

            if not parts:
                continue

            target_path = output_dir.joinpath(*parts)

            # If full path is still too long, flatten filename
            if len(str(target_path)) > MAX_FULL_PATH:
                file_name = shorten_name("_".join(parts), 100)
                target_path = output_dir / file_name

            if item.is_dir():
                target_path.mkdir(parents=True, exist_ok=True)
            else:
                target_path.parent.mkdir(parents=True, exist_ok=True)

                with zf.open(item) as source, open(target_path, "wb") as target:
                    target.write(source.read())

            print("Extracted:", target_path)


safe_extract(ZIP_FILE, OUTPUT_DIR)