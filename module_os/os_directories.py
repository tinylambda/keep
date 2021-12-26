import os

if __name__ == '__main__':
    dir_name = 'os_directories_example'

    print(f'Creating {dir_name}')
    os.makedirs(dir_name)

    file_name = os.path.join(dir_name, 'example.txt')
    print(f'Creating {file_name}')
    with open(file_name, 'wt') as f:
        f.write('example file')

    print('Cleaning up')
    os.unlink(file_name)
    os.rmdir(dir_name)
