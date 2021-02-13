def print_actor():
    while True:
        try:
            msg = yield
            print('Got: ', msg)
        except GeneratorExit:
            print('Actor terminating')
            raise


if __name__ == '__main__':
    p = print_actor()
    next(p)
    p.send('hello')
    p.send('world')
    p.close()

