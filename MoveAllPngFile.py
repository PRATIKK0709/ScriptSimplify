import os
import shutil

def move_png_files_to_new_folder():
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")
    new_folder_name = "PNG_Files"
    new_folder_path = os.path.join(current_directory, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    print(f"Created a new folder: {new_folder_name}")
    file_list = os.listdir(current_directory)

    for file_name in file_list:
        if file_name.lower().endswith('.png'):
            file_path = os.path.join(current_directory, file_name)
            new_file_path = os.path.join(new_folder_path, file_name)
            shutil.move(file_path, new_file_path)
            print(f"Moved {file_name} to {new_folder_name}")

if __name__ == "__main__":
    move_png_files_to_new_folder()
