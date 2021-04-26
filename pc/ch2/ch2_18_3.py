import re

from ch2_18_2 import generate_tokens


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))
for token in generate_tokens(master_pat, 'printer'):
    print(token)

