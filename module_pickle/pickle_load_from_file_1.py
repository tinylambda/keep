import pickle
import pprint
import sys

from module_pickle.pickle_dump_to_file_1 import SimpleObject

filename = sys.argv[1]

with open(filename, 'rb') as in_s:
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print('READ: {} ({})'.format(o.name, o.name_backwards))

