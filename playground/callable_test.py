class A:
    def __init__(self):
        print("I am in __init__")

    def __call__(self, *args, **kwargs):
        print("I am in __call__")


if __name__ == "__main__":
    a = A()
    print("delimiter")
    a()
