import os

def rename_file(old_name, new_name):
    try:
        if not os.path.exists(old_name):
            err = f"File {old_name} doesn't exist"
            return False, err
        if os.path.exists(new_name):
            counter = 1
            base,ext = os.path.splitext(new_name)
            while os.path.exists(new_name):
                new_name = f"{base}({counter}){ext}"
                counter +=1
        os.rename(old_name, new_name)
        return True, new_name
    except Exception as e:
        err = f"An error occured: {e}"
        return False, err