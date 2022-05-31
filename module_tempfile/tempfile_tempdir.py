import tempfile

tempfile.tempdir = "/I/Changed/this/Path"
print("gettempdir():", tempfile.gettempdir())
