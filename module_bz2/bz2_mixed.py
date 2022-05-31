import bz2

lorem = open("lorem.txt", "rb").read()
compressed = bz2.compress(lorem)
combined = compressed + lorem

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print("decompressed matches lorem: ", decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print("unused data matches lorem:", unused_matches)
