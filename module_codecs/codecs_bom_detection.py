import codecs
from module_codecs.codecs_to_hex import to_hex


# Look at the raw data
with open('nonnative-encoded.txt', mode='rb') as f:
    raw_bytes = f.read()

print('Raw: ', to_hex(raw_bytes, 2))

# Re-open the file and let codecs detect the BOM
with codecs.open('nonnative-encoded.txt', mode='r', encoding='utf-16') as f:
    decoded_text = f.read()

print('Decoded: ', decoded_text)

# Open the file use builtin open function
with open('nonnative-encoded.txt', mode='r', encoding='utf-16') as f:
    print(f.read())

