import zipfile


with zipfile.ZipFile("example.zip") as zf:
    for filename in ["zipfile_is_zipfile.py", "README.txt"]:
        try:
            data = zf.read(filename)
        except KeyError:
            print("ERROR: did not find {} in zip file".format(filename))
        else:
            print(filename, ":")
            print(data)
        print()
