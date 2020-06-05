import io
import os
import shutil
import sys


class VerboseStringIO(io.StringIO):
    def read(self, n=-1):
        _next = io.StringIO.read(self, n)
        print('read({}) got {} bytes'.format(n, len(_next)))
        return _next


lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit.  Vestibulum aliquam mollis dolor. Donec
vulputate nunc ut diam. Ut rutrum mi vel sem. Vestibulum
ante ipsum.'''

print('Default: ')
_input = VerboseStringIO(lorem_ipsum)
_output = io.StringIO()
shutil.copyfileobj(_input, _output)

print()

print('All at once: ')
_input = VerboseStringIO(lorem_ipsum)
_output = io.StringIO()
shutil.copyfileobj(_input, _output, -1)

print()

print('Blocks of 256: ')
_input = VerboseStringIO(lorem_ipsum)
_output = io.StringIO()
shutil.copyfileobj(_input, _output, 256)

