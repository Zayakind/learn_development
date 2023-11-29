import os


def search_files(directory, files: list):

    # name_dir = os.listdir(directory)
    #
    # [files.append(name) if os.path.isfile(name) and "." in name else search_files(name, files) for name in name_dir]

    for dir_path, dir_names, filenames in os.walk(directory):
        [files.append(file) for file in filenames]

        for dir in dir_names:
            search_files(os.path.join(dir_path, dir), files)


def find_files(directory):
    files = []

    search_files(directory, files)
    return files
