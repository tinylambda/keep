import sys
from pprint import pprint


pprint(sys.meta_path)


class Finder:
    def find_module(self, fullname, path):
        print("looking for", fullname, path)
        return None


sys.meta_path.insert(0, Finder())

import math
import types  # no output ?
import threading

import xml.etree.ElementTree

print("*" * 32)

del sys.meta_path[0]
sys.meta_path.append(Finder())
import urllib.request
import datetime

import fib
