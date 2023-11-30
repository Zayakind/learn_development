import os


def find_files(directory):
    files = []
    entries = os.listdir(directory)
    for entry in entries:
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            files.append(entry)
        if os.path.isdir(full_path):
            files.extend(find_files(full_path))
    return files
