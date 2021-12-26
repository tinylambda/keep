import os


if __name__ == '__main__':
    link_name = os.path.join('/tmp', os.path.basename(__file__))
    print(f'Creating link {link_name} -> {__file__}')
    os.symlink(__file__, link_name)

    stat_info = os.lstat(link_name)
    print(f'Permissions: {oct(stat_info.st_mode)}')
    print(f'Points to: {os.readlink(link_name)}')

    os.unlink(link_name)
