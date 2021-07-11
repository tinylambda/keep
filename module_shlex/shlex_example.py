import shlex
import sys

if len(sys.argv) != 2:
    print('please specify one filename on the command line.')
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as f:
    body = f.read()

print('original: {!r}'.format(body))
print()

print('tokens:')
lexer = shlex.shlex(body)
for token in lexer:
    print('{!r}'.format(token))

