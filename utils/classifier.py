import os


file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".svg", ".heic", ".heif", ".raw", ".cr2", ".nef", ".ico"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".pages",".xls", ".xlsx", ".pptx", ".csv", ".numbers", ".key",".rtf",".ppt", ".pptx", ".ods",".epub",".md", ".tex"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a",".m4v", ".3gp",".wma"],
    "Archive" : [".zip", ".rar", ".7z", ".tar", ".gz",".bz2",".xz"],
    
    
}
def classify_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    for category,extensions in file_types.items():
        if ext in extensions:
            return category
    return "Others"