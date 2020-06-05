import shutil


for _format, exts, description in shutil.get_unpack_formats():
    print('{:<5}: {}, names ending in {}'.format(_format, description, exts))

