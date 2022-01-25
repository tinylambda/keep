import pprint

from papa import Papa

if __name__ == '__main__':
    with Papa() as p:
        pprint.pprint('Default')
        pprint.pprint(p.list_sockets())

        pprint.pprint('with prefix')
        pprint.pprint(p.list_sockets('uwsgi*'))

        pprint.pprint('with name')
        pprint.pprint(p.list_sockets('uwsgi2'))
