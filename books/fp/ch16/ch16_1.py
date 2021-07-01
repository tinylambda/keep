def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)


if __name__ == '__main__':
    m_coro = simple_coroutine()
    print(m_coro)
    next(m_coro)
    m_coro.send(42)


