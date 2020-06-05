import shutil


for _format, description in shutil.get_archive_formats():
    print('{:<5}: {}'.format(_format, description))

