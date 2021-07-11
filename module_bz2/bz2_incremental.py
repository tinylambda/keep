import bz2
import binascii
import io

compressor = bz2.BZ2Compressor()

with open('lorem.txt', 'rb') as f:
    while True:
        block = f.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('compressed: {}'.format(binascii.hexlify(compressed)))
        else:
            print('buffering')
    remaining = compressor.flush()
    print('flushed: {}'.format(binascii.hexlify(remaining)))




