from tempfile import NamedTemporaryFile


with NamedTemporaryFile('w+t') as f:
    print('filename:', f.name)
    f.write('hello world\n')
    f.write('!\n')

    f.seek(0)
    data = f.read()
    print(data)


with NamedTemporaryFile('w+t', delete=False) as f:
    print(f'filename:', f.name)
    f.write('do not delete me!')
    f.write('!!!\n')

    f.seek(0)
    data = f.read()
    print(data)

