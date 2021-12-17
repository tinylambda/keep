import os.path

PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]

if __name__ == '__main__':
    for parts in PATHS:
        print('{} : {!r}'.format(parts, os.path.join(*parts)))
