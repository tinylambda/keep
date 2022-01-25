from pprint import pprint

from papa import Papa

if __name__ == '__main__':
    with Papa() as p:
        pprint('Before remove socket')
        pprint(p.list_sockets())

        try:
            p.remove_sockets('uwsgi')
        except Exception as e:
            pprint(e)

        pprint('After remove socket')
        pprint(p.list_sockets())

        pprint('Processes')
        pprint(p.list_processes())
