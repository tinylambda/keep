import unicodedata
from module_codecs.codecs_to_hex import to_hex


text = '中国'

print('Raw: {!r}'.format(text))
for c in text:
    print(' {!r}: {}'.format(c, unicodedata.name(c, c)))
print('UTF-8: {!r}'.format(to_hex(text.encode('utf-8'), 1)))
print('UTF-16: {!r}'.format(to_hex(text.encode('utf-16'), 2)))

