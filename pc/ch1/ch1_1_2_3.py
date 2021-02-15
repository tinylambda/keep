if __name__ == '__main__':
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    line = 'root:x:0:0:root:/root:/bin/bash'
    uname, *fields, homedir, sh = line.split(':')
    print(uname)
    print(homedir)
    print(sh)

    record = ['ACME', 50, 123.45, (12, 18, 2012)]
    name, *_, (*_, year) = record
    print(name)
    print(year)

    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items
    print(head)
    print(tail)

    def sum(items):
        head, *tail = items
        return head + sum(tail) if tail else head

    print(sum(items))

