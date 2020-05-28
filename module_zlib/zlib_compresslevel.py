import zlib


input_data = b'Some repeated text.\n' * 1024
template = '{:>5}  {:>5}'
print(template.format('Level', 'Size'))
print(template.format('-' * 5, '-' * 5))

for i in range(0, 10):
    data = zlib.compress(input_data, i)
    print(template.format(i, len(data)))

