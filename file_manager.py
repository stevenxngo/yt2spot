import shutil
import os


def move_to_folder(file_path, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    dest_path = os.path.join(folder_path, os.path.basename(file_path))
    shutil.move(file_path, dest_path)
    return dest_path
