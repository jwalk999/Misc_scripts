"""
File Name: renamer.py
Author: Jonathan W.
Date: 11/10/2026
Scope: A simple script to batch rename multiple files using the modified date. 
"""

import datetime
from pathlib import Path

ORIGINALS = Path("~/originals/")
RENAMED = Path("~/renamed/")

def file_rename(original_path: Path, new_path: Path) -> None:
    """Move and rename files to '<modified date>.<extension>'.

    If a name already exists, a counter is added to keep it unique.

    Args:
        original_path: Folder containing the original files.
        new_path: Folder where the renamed files will be moved.
    """
    new_path.mkdir(exist_ok=True)  # create the folder if it's missing

    files = [f for f in original_path.iterdir() if f.is_file()]

    for old_file in sorted(files):
        modified = datetime.datetime.fromtimestamp(old_file.stat().st_mtime)
        date_str = modified.strftime("%Y-%m-%d_%H%M%S")

        new_file = new_path / f"{date_str}{old_file.suffix}"

        # Only add a counter if that name is already taken
        counter = 1
        while new_file.exists():
            new_file = new_path / f"{date_str}_{counter}{old_file.suffix}"
            counter += 1

        old_file.rename(new_file)


file_rename(ORIGINALS, RENAMED)