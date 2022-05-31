import gzip
from io import BytesIO
import binascii


uncompressed_data = b"The same line, over and over.\n" * 10
print("UNCOMPRESSED: ", len(uncompressed_data))
print(uncompressed_data)

buf = BytesIO()
with gzip.GzipFile(mode="wb", fileobj=buf) as f:
    f.write(uncompressed_data)

compressed_data = buf.getvalue()
print("COMPRESSED: ", len(compressed_data))
print(binascii.hexlify(compressed_data))

inbuffer = BytesIO(compressed_data)
with gzip.GzipFile(mode="rb", fileobj=inbuffer) as f:
    reread_data = f.read(len(uncompressed_data))

print("\nREREAD: ", len(reread_data))
print(reread_data)


# One benefit of using GzipFile over zlib is that it supports the file API. However, when re-reading the previously
# compressed data, an explicit length is passed to read(). Leaving the length off resulted in a CRC error, possibly
# because BytesIO returned an empty string before reporting EOF. When working with streams of compressed data, either
# prefix the data with an integer representing the actual amount of data to be read or use the incremental decompression
# API in zlib.
