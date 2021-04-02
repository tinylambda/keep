import os


# open a low-level file descriptor
fd = os.open('sample.txt', os.O_WRONLY | os.O_CREAT)
print(fd)

f = open(fd, 'wt', closefd=False)
f.write('hello world\n')
f.close()  # auto close fd if not set closed=False in open()

f2 = open(fd, 'wt')
f2.write('!')
f2.close()

