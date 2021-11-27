import shutil
import os

source = "/Users/Swarnali/Desktop/folder A/"
destination = "/Users/Swarnali/Desktop/folder B/"
files = os.listdir (source)

for i in files:
    shutil.move(source+i, destination)
