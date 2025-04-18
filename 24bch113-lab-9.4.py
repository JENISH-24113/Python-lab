import os
import shutil

source_dir = "source_folder"
target_dir = "target_folder"
file_to_copy = "example.txt"

os.makedirs(target_dir, exist_ok=True)
shutil.copy(os.path.join(source_dir, file_to_copy), target_dir)

print("File copied successfully.")