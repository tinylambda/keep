import os
import sys


print(sys.getdefaultencoding())

# Write a file using a unicode file
with open('jalapeño.txt', 'w') as f:
    f.write('Spicy!')


print(os.listdir(''))
print(os.listdir(b''))

with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

