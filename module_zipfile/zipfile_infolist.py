import datetime
import zipfile


def print_info(archive_name):
    with zipfile.ZipFile(archive_name) as zf:
        for info in zf.infolist():
            print(info.filename)
            print('\tComment\t:', info.comment)
            mod_date = datetime.datetime(*info.date_time)
            print('\tModified\t:', mod_date)
            if info.create_system == 0:
                system = 'windows'
            elif info.create_system == 3:
                system = 'unix'
            else:
                system = 'unknown'
            print('\tSystem\t:', system)
            print('\tZip Version\t:', info.create_version)
            print('\tCompressed\t:', info.compress_size, 'bytes')
            print('\tUncompressed\t:', info.file_size, 'bytes')
            print()


if __name__ == '__main__':
    print_info('example.zip')

