from contextvars import ContextVar, Token

if __name__ == '__main__':
    var: ContextVar[str] = ContextVar('var')
    token: Token = var.set('new value')
    print(var.get())

    var.reset(token)
    try:
        print(var.get())
    except LookupError:
        print('LookupError')
