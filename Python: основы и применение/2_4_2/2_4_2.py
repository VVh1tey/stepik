import os
import zipfile

def find_directories(root_directory):
    directories = []

    for dirpath, dirnames, filenames in os.walk(root_directory):
        python_files = [filename for filename in filenames if filename.endswith('.py')]
        if python_files:
            path = os.path.relpath(dirpath, root_directory)
            directories.append(path)

    return sorted(directories)

with zipfile.ZipFile('main.zip', 'r') as zip:
    zip.extractall('main')

dirs = find_directories('main')

with open('output.txt', 'w') as file:
    for dir in dirs:
        file.write(dir + '\n')