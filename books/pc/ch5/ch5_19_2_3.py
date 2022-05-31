import os
from tempfile import TemporaryDirectory, SpooledTemporaryFile


with TemporaryDirectory() as dirname:
    print("dirname is:", dirname)
    os.mkdir(os.path.join(dirname, "test"))
    print(os.listdir(dirname))


print(os.listdir(dirname))  # no such file or directory
