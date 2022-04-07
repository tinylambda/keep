import subprocess


if __name__ == '__main__':
    try:
        # This example does not set check=True so the output of the command is captured and printed.
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('Have {} bytes in stdout: {!r}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))
        print('Have {} bytes in stderr: {!r}'.format(len(completed.stderr), completed.stderr.decode('utf-8')))
