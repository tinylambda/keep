import mmap
import shutil


# Copy the example file
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
_reversed = word[::-1]

# It is necessary to rewind the file handle in this example separately from the mmap handle,
# because the internal state of the two objects is maintained separately.
with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY) as m:
        print('Memory Before: \n{}'.format(m.readline().rstrip()))
        print('File Before: \n{}\n'.format(f.readline().rstrip()))

        m.seek(0)  # rewind
        loc = m.find(word)
        m[loc: loc + len(word)] = _reversed

        m.seek(0)  # rewind
        print('Memory After: \n{}'.format(m.readline().rstrip()))
        f.seek(0)
        print('File After: \n{}'.format(f.readline().rstrip()))

