import tarfile


with tarfile.open("/Users/Felix/Downloads/django.tar.gz", "r") as t:
    print(t.getnames())
