import tarfile

for filename in [
    "__init__.py",
    "example.tar",
    "/Users/Felix/Downloads/django.tar.gz",
    "/Users/Felix/Downloads/test.tar.gz",
]:
    try:
        print("{:>15} {}".format(filename, tarfile.is_tarfile(filename)))
    except IOError as err:
        print("{:>15} {}".format(filename, err))
