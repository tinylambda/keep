import os
import pprint

import papa
from papa import Papa


class MyObject:
    def __init__(self):
        self.papa = Papa()

    def start_stuff(self):
        self.papa.make_socket('uwsgi')
        with open('/tmp/uwsgi.ini', 'w') as f:
            pass

        self.papa.make_process(
            'uwsgi', 'uwsgi',
            args=('--ini', 'uwsgi.ini', '--socket', 'fd://$(socket.uwsgi.fileno)'),
            working_dir='/tmp', env=os.environ)

    def close(self):
        self.papa.close()


if __name__ == '__main__':
    my_object = None

    try:
        my_object = MyObject()
        my_object.start_stuff()
    finally:
        if my_object is not None:
            my_object.close()

    def show_papa():
        papa = Papa()
        pprint.pprint(papa.list_processes())
        pprint.pprint(papa.list_sockets())
        pprint.pprint(papa.list_values())

    show_papa()
    