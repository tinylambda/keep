from coroutine import coroutine


@coroutine
def grep(pattern):
    print(f'looking for {pattern}')
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('going away. goodbye')


if __name__ == '__main__':
    g = grep('python')
    g.send('hello')
    g.send('world')
    g.send('python go')
    g.send('bye')
    # throw Exception from the yield expression
    g.throw(RuntimeError, 'run time error you know')
    g.close()

