import tempfile


with tempfile.TemporaryFile() as temp:
    temp.write(b"some data")
    temp.seek(0)
    print(temp.read())
