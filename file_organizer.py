import os, shutil, datetime, pathlib

directory_to_organize = "/Users/mustafahussain/Desktop/cachehw"

SUBDIRECTORIES = {
    "Python File" : ['.py', '.java'],
    "Documents" : [".pdf"],
    "Video Files": ['.mov','.mp4'],
    "Images": ['.jpg','.jpeg','.png', '.heic'],
    "Microsoft Suite Files" : ['.docx', '.xlsx', '.pptx'],
    "Zip/Tar files": ['.tar']
}
def directorySelector(suffix):
    for category, suffixes in SUBDIRECTORIES.items():
        if suffix.lower() in suffixes:
            return category
    return "Miscellaneous"

def organizeFiles(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            continue
        file_extension = os.path.splitext(filename)[1]
        folder = directorySelector(file_extension)
        print(f"{filename} ➝ {folder}")
        target_folder = os.path.join(directory, folder)
        os.makedirs(path, exist_ok=True)
        destination = os.path.join(target_folder, filename)
        shutil.move(path, destination)

organizeFiles(directory_to_organize)
