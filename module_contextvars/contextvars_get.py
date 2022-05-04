from contextvars import ContextVar

if __name__ == '__main__':
    var: ContextVar[int] = ContextVar('var', default=47)
    print(var.get())
    var.set(100)
    print(var.get())
