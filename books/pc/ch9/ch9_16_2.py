from inspect import Signature, Parameter


if __name__ == "__main__":
    params = [
        Parameter("x", Parameter.POSITIONAL_OR_KEYWORD),
        Parameter("y", Parameter.POSITIONAL_OR_KEYWORD, default=87),
        Parameter("z", Parameter.KEYWORD_ONLY, default=None),
    ]
    sig = Signature(params)
    print(sig)

    def func(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            print(name, value)

    func(1, 2, z=3)
    print("-" * 64)
    func(1)
    print("-" * 64)
    func(1, z=3)
    print("-" * 64)
    func(y=2, x=1)
    print("-" * 64)
    try:
        func(1, 2, 3, 4)
    except TypeError as e:
        print(e)

    print("-" * 64)
    try:
        func(1, y=2, x=3)
    except TypeError as e:
        print(e)
