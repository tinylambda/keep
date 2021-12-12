from pprint import pprint

from module_pprint.pprint_data import data

if __name__ == '__main__':
    print('DEFAULT:')
    pprint(data, compact=False)
    print('\nCOMPACT:')
    pprint(data, compact=True)
