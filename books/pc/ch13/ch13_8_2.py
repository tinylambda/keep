import shutil


shutil.make_archive('/tmp/py3', 'zip', 'tmp')
shutil.make_archive('/tmp/py3', 'bztar', 'tmp')
shutil.make_archive('/tmp/py3', 'gztar', 'tmp')
shutil.make_archive('/tmp/py3', 'tar', 'tmp')

print(shutil.get_archive_formats())
