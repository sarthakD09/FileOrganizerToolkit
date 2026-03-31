from file_ops.mover import move_file
from file_ops.renamer import rename_file 
from file_ops.scanner import scan_directory  
from utils.classifier import classify_file
import os
import argparse

def organize_directory(directory, dry_run, logger=None):
    def log(message):
        if logger:
            logger(message)
        else:
            print(message)

    # Validate directory
    if not os.path.isdir(directory):
        return False, f"Directory '{directory}' does not exist"

    if os.path.abspath(directory) in ["/", os.path.expanduser("~")]:
        return False, "Refusing to organize critical directory"

    # Scan directory
    success, result = scan_directory(directory)
    if not success:
        return False, result

    files = result
    total_files = len(files)
    files_moved = 0

    for file_path in files:
        filename = os.path.basename(file_path)

        # Skip hidden files
        if filename.startswith('.'):
            continue

        # Skip non-files
        if not os.path.isfile(file_path):
            continue

        category = classify_file(file_path)
        destination_dir = os.path.join(directory, category)

        # Skip already organized files
        if os.path.dirname(file_path) == destination_dir:
            continue

        action_msg = f"{file_path} → {destination_dir}"

        if dry_run:
            files_moved += 1
            log(f"[DRY RUN] {action_msg} ({files_moved}/{total_files})")
            continue

        # Actual move
        success, msg = move_file(file_path, destination_dir)

        if success:
            files_moved += 1
            log(f"[MOVED] {action_msg} ({files_moved}/{total_files})")
        else:
            log(f"[ERROR] {msg}")

    return True, f"Processed {total_files} files, moved {files_moved}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Organizer Tool")

    parser.add_argument("--path", required=True, help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without moving files")

    args = parser.parse_args()

    path = os.path.abspath(os.path.expanduser(args.path))

    if not os.path.isdir(path):
        print("Invalid directory")
        exit(1)

    success, msg = organize_directory(path, dry_run=args.dry_run)

    if success:
        print(msg)
    else:
        print(f"Error: {msg}")