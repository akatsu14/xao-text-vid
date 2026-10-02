from __future__ import annotations

import argparse
from pathlib import Path


def process_file(file_path: Path) -> bool:
    """Remove * and #, then return whether the cleaned file ends with . or ? or !."""
    text = file_path.read_text(encoding="utf-8-sig")
    cleaned_text = text.replace("*", "").replace("#", "")

    if cleaned_text != text:
        file_path.write_text(cleaned_text, encoding="utf-8")

    return cleaned_text.rstrip().endswith((".", "?", "!"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove * and # from text files and check the final punctuation."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        help="Local folder path to process. If omitted, you will be prompted.",
    )
    args = parser.parse_args()

    folder_text = args.folder or input("Paste the folder path: ").strip()
    folder_path = Path(folder_text.strip('"'))

    if not folder_path.is_dir():
        parser.error(f"Folder does not exist: {folder_path}")

    processed_count = 0
    missing_punctuation = []

    for file_path in folder_path.rglob("*.txt"):
        try:
            has_punctuation = process_file(file_path)
        except (OSError, UnicodeError) as error:
            print(f"ERROR: {file_path} - {error}")
            continue

        processed_count += 1
        if not has_punctuation:
            missing_punctuation.append(file_path)

    print(f"Processed: {processed_count} file(s)")
    if missing_punctuation:
        print("Files without final punctuation (. or ?):")
        for file_path in missing_punctuation:
            print(f"- {file_path}")
    else:
        print("All files end with . or ?")


if __name__ == "__main__":
    main()