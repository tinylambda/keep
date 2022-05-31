import tarfile


with tarfile.open("/Users/Felix/Downloads/django.tar.gz", "r") as t:
    for filename in [
        "django/tests/admin_docs/views.py",
        "django/tests/admin_docs/models.py",
    ]:
        try:
            f = t.extractfile(filename)
        except KeyError:
            print("ERROR: did not find {} in tar file".format(filename))
        else:
            print(filename, ":")
            print(f.read().decode("utf-8"))
