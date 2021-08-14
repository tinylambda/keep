import traceback
import sys

from books.pc.ch14.ch14_12_2 import func

try:
    func('hello')
except Exception as e:
    print('**** an error occurred')
    traceback.print_exc(file=sys.stderr)
