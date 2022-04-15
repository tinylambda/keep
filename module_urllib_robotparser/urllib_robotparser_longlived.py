from urllib import robotparser
import time


if __name__ == '__main__':
    AGENT_NAME = 'PyMOTW'
    parser = robotparser.RobotFileParser()
    parser.set_url('file:robots.txt')
    parser.read()
    parser.modified()

    PATHS = [
        '/',
        '/PyMOTW/',
        '/admin/',
        '/downloads/PyMOTW-1.92.tar.gz',
    ]

    for path in PATHS:
        age = int(time.time() - parser.mtime())
        print('age: ', age, end=' ')
        if age > 1:
            print('rereading robots.txt')
            parser.read()
            parser.modified()
        else:
            print()
        print('{!r:>6}: {}'.format(parser.can_fetch(AGENT_NAME, path), path))
        time.sleep(1)
        print()
