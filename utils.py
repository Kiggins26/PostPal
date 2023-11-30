import os

def get_image_files(dir_path):
    
    image_files = []
    for file in dir_path:
        if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
            image_files.append(file)
    return image_files
