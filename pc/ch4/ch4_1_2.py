with open('/etc/passwd', 'r') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

print('-' * 64)

with open('/etc/passwd', 'r') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

