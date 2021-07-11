import zipfile


with zipfile.ZipFile('example.zip') as zf:
    for filename in ['zipfile_is_zipfile.py']:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print('ERROR: did not find {} in zip file'.format(filename))
        else:
            print('{} is {} bytes'.format(info.filename, info.file_size))

