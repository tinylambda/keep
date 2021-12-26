import os


TEST_GID = 502
TEST_UID = 502


def show_user_info():
    print(f'User (actual/effective): {os.getuid()} / {os.geteuid()}')
    print(f'Group (actual/effective: {os.getgid()} / {os.getegid()}')
    print(f'Actual groups: {os.getgroups()}')


if __name__ == '__main__':
    TEST_GID = 1000
    TEST_UID = 1000

    print('Before change')
    show_user_info()
    print()

    try:
        os.setegid(TEST_GID)
    except OSError:
        print('ERROR: could not change effective group. rerun as root.')
    else:
        print('CHANGE GROUP:')
        show_user_info()
        print()

    try:
        os.seteuid(TEST_UID)
    except OSError:
        print('ERROR: could not change effective user. rerun as root')
    else:
        print('CHANGE USER:')
        show_user_info()
        print()
