import os

def get_image_files(dir_path):
    image_files = []
    for file in os.listdir(dir_path):
        if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
            image_files.append(os.path.join(dir_path, file))
    return image_files

