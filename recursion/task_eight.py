import os


def search_files(directory, files: list):

    entries = os.listdir(directory)
    for entry in entries:
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            files.append(full_path)
        elif os.path.isdir(full_path):
            search_files(full_path, files)


def find_files(directory):
    files = []
    search_files(directory, files)
    return files
