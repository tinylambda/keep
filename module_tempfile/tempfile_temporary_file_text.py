import tempfile


with tempfile.TemporaryFile(mode="w+t") as temp:
    temp.writelines(["first\n", "second\n"])
    temp.seek(0)
    for line in temp:
        print(line.strip())
