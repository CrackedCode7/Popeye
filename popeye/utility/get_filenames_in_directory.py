import os

def get_filenames_in_directory(directory_path):
    
    filenames = []
    for filename in os.listdir(directory_path):
        path = os.path.join(directory_path, filename)
        if os.path.isfile(path):
            filenames.append(path)

    return filenames