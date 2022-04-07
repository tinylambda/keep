import subprocess


if __name__ == '__main__':
    completed = subprocess.run('echo $HOME', shell=True)
    print('returncode:', completed.returncode)
