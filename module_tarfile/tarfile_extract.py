import tarfile
import os

outdir = "/tmp/outdir"

if not os.path.exists(outdir):
    os.mkdir(outdir)

with tarfile.open("/Users/Felix/Downloads/django.tar.gz", "r") as t:
    t.extract("django/tests/admin_docs/views.py", outdir)

print(os.listdir("/tmp/outdir"))
