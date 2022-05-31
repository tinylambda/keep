import zipfile


with zipfile.ZipFile("example.zip", "r") as zf:
    print(zf.namelist())
