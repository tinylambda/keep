import tarfile
import time

with tarfile.open('/Users/Felix/Downloads/django.tar.gz', 'r') as t:
    for filename in ['django/tests/admin_docs/views.py', 'django/tests/admin_docs/models.py']:
        try:
            info = t.getmember(filename)
        except KeyError:
            print('ERROR: did not find {} in tar archive'.format(filename))
        else:
            print('{} is {:d} bytes'.format(info.name, info.size))

