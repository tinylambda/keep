from pprint import pprint

from module_pprint.pprint_data import data

if __name__ == '__main__':
    for width in [80, 5]:
        print('WIDTH =', width)
        pprint(data, width=width)
        print()
