import zlib
import binascii


compressor = zlib.compressobj(1)
with open('/tmp/stop_easyconnect.sh', 'rb') as input_data:
    while True:
        block = input_data.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressed: {}'.format(
                binascii.hexlify(compressed)
            ))
        else:
            print('buffering...')
    remaining = compressor.flush()
    print('Finished: {}'.format(binascii.hexlify(remaining)))

