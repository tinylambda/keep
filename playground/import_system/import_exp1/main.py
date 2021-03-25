class Finder:
    def find_loader(self, name):
        print('Looking for', name)
        return None, []


import sys
sys.path_importer_cache['debug'] = Finder()
sys.path.insert(0, 'debug')

import threading

