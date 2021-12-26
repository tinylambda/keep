import os

if __name__ == '__main__':
    child_pid = os.fork()
    if child_pid:
        os.waitpid(child_pid, 0)
        print('Child done')
    else:
        os.execlp('pwd', 'pwd', '-P')
