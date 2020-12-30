def f(x):
    print(x, type(x))


def f2(x):
    print(x, type(x))


f2 = classmethod(f2)


example_cls = type(
    'example_cls',
    (),
    {'f': f, 'f2': f2}
)

example_instance = example_cls()
example_instance.f()

example_cls.f2()
example_instance.f2()

