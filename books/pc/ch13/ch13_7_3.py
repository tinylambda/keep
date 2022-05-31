import os.path


filename = "/Users/guido/programs/spam.py"
print(os.path.basename(filename))
print(os.path.dirname(filename))
print(os.path.split(filename))
print(os.path.join("/new/dir", os.path.basename(filename)))
print(os.path.expanduser("~/guido/programs/spam.py"))
