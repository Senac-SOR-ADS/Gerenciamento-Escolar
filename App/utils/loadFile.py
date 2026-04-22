import sys
from os import path

def loadFile(file):
    base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
    print(globals())
    print(base_path, file)
    return path.join(base_path, file)