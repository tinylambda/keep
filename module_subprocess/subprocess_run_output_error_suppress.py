import subprocess


if __name__ == '__main__':
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('stdout is {!r}'.format(completed.stdout))
        print('stderr is {!r}'.format(completed.stderr))
