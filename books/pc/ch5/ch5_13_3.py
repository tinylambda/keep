import os
import os.path
import glob


pyfiles = glob.glob("*.py")
name_sz_date = [
    (name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles
]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

print("-" * 64)

file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
