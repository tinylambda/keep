import argparse


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands', dest='command')

list_parser = subparsers.add_parser('list', help='list contents')
list_parser.add_argument('dirname', action='store', help='directory to list')

create_parser = subparsers.add_parser('create', help='create a directory')
create_parser.add_argument('driname', action='store', help='new directory to create')
create_parser.add_argument('--readonly', default=False, action='store_true',
                           help='set permissions to prevent writing to the directory')
delete_parser = subparsers.add_parser('delete', help='remove a directory')
delete_parser.add_argument('dirname', action='store', help='the directory to remove')
delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
                           help='remove the contents of the directory, too')

ns = parser.parse_args()
print(ns)
print()

# python argparse_subparsers.py -h
# python argparse_subparsers.py list -h
