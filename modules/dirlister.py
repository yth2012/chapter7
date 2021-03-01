import os

def run(**args):
    print("[*] in dirlister")
    files = os.listdir(os.getcwd())
    return str(files)