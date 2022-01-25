import os
import pprint

from papa import Papa

if __name__ == '__main__':
    with Papa() as p:
        pprint.pprint(p.list_processes())
        pprint.pprint(p.make_socket('uwsgi2', port=10020))
        pprint.pprint(p.list_sockets())
        pprint.pprint(p.make_process('uwsgi2', 'uwsgi', args=('--ini', 'uwsgi.ini',
                                     '--socket', 'fd://$(socket.uwsgi2.fileno)'), working_dir='/tmp', env=os.environ))
        pprint.pprint(p.make_process('uwsgi22', 'uwsgi', args=('--ini', 'uwsgi.ini',
                                                               '--socket', 'fd://$(socket.uwsgi2.fileno)'),
                                     working_dir='/tmp', env=os.environ))
        pprint.pprint(p.list_processes())
