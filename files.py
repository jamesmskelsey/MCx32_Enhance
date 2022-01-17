import os

def get_files(dir):
    # allow for a default value of a function call
    if not dir:
        dir = os.getcwd()
    files = os.listdir(dir)
    files = list(file for file in files if file[-4:] == ".png")
    return files
