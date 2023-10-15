from PIL import Image
import os

def convert_all_files_to_png_in_current_directory():
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")

    file_list = os.listdir(current_directory)

    for file_name in file_list:
        file_path = os.path.join(current_directory, file_name)

        try:
            with Image.open(file_path) as image:
                output_file_path = os.path.splitext(file_path)[0] + '.png'
                image.save(output_file_path, 'PNG')
                print(f"Converted {file_name} to {os.path.basename(output_file_path)}")
        except Exception as e:
            print(f"Skipped {file_name}: {str(e)}")
if __name__ == "__main__":
    convert_all_files_to_png_in_current_directory()
