import re


if __name__ == '__main__':
    line = 'asdf fjdk; afed, fjek,asdf,    foo'
    result = re.split(r'[;,\s]\s*', line)
    print(result)

    print('-' * 64)

    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)

    values = fields[::2]
    print(values)
    delimiters = fields[1::2] + ['']
    print(delimiters)

    print(''.join(v+d for v, d in zip(values, delimiters)))

    print('-' * 64)
    print(re.split(r'(?:,|;|\s)\s*', line))  # non-capture group

