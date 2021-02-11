if __name__ == '__main__':
    with open('__init__.py') as fp:
        src = fp.read()

    print(len(src))
    print(fp)
    print(fp.closed, fp.encoding)

    fp.read()

