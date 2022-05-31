import glob
import os
import shutil


os.mkdir("example")
print("Before: ", glob.glob("example/*"))

shutil.copy("shutil_copy.py", "example")

print("After: ", glob.glob("example/*"))
