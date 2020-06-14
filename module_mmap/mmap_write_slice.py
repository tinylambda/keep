import mmap
import shutil


# Copy the example file
shutil.copy('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
_reversed = word[::-1]
print('Looking for: ', word)
print('Replacing with: ', _reversed)

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # rewind

        loc = m.find(word)
        m[loc: loc + len(word)] = _reversed
        m.flush()

        m.seek(0)
        print('After: \n{}'.format(m.readline().rstrip()))

        f.seek(0)  # rewind
        print('File: \n{}'.format(f.readline().rstrip()))

