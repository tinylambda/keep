import subprocess


if __name__ == '__main__':
    print('write:')
    proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
    )
    proc.communicate('stdin: to stdin\n'.encode('utf-8'))
