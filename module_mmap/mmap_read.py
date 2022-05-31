import mmap


#  It is then reset to the beginning of the file by the slice operation, and moved ahead 10 bytes again by the slice.
with open("lorem.txt", "rt") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print("First 10 bytes via read: ", m.read(10))
        print("First 10 bytes via slice: ", m[:10])
        print("2nd 10 bytes via read: ", m.read(10))
