class A:
    def __getattribute__(self, item):
        print(f"Getting {item}")


class B:
    pass


if __name__ == "__main__":
    b = B()
    b.state  # AttributeError: 'B' object has no attribute 'state'

    a = A()
    getattr(a, "state.s1")
    a.state.s1  # NoneType object has not attribute 's1'
