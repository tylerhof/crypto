import os

def map_file(file, map, read_mode = "rb", write_mode = "wb"):
    with open(file, read_mode) as f:
        mapped_file = map(f.read())
    with open(file, write_mode) as f:
        f.write(mapped_file)

def map_folder(folder, map, read_mode = "rb", write_mode = "wb"):
    for dirpath, dirs, files in os.walk(folder):
        for file in files:
            if (not ".git" in dirpath):
                map_file(os.path.abspath(os.path.join(dirpath, file)), map, read_mode, write_mode)