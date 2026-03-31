import os

def scan_directory(directory):
    try:
        if not os.path.isdir(directory):
            err = f"Directory {directory} doesn't exist"
            return False, err
        onlyfiles = [f.path for f in os.scandir(directory) if f.is_file()]
        return True, onlyfiles
    except Exception as e:
        err = f"An error occured: {e}"
        return False, err
