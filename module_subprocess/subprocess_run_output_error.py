import subprocess


if __name__ == '__main__':
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('Have {} butes in stdout: {!r}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))
