import pprint

from papa import Papa

if __name__ == '__main__':
    with Papa() as p:
        p.make_socket('circus.uwsgi', path='/tmp/uwsgi.sock')
        pprint.pprint(p.list_sockets())
