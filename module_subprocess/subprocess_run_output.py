import subprocess


if __name__ == '__main__':
    # Passing check=True and setting stdout to PIPE is equivalent to using check_output().
    completed = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout:\n{}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))
