import shutil
import os

def move_file(src,dst):
    try:
        if not os.path.exists(src):
                err = f"File {src} doesn't exist"
                return False, err
        
        os.makedirs(dst, exist_ok = True)
        filename = os.path.basename(src)
        final_path = os.path.join(dst, filename)
        #handling duplicates
        if os.path.abspath(src) == os.path.abspath(final_path):
            return False, "Source and destination are the same"
        if os.path.exists(final_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(final_path):
                new_filename = f"{base}({counter}){ext}"
                final_path = os.path.join(dst, new_filename)
                counter +=1
        shutil.move(src, final_path)
        return True, final_path
    except Exception as e:  
        err = f"An error occured: {e}"
        return False, err
