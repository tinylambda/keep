class A:
    @classmethod
    @property
    def myname(cls):
        return "hi"


if __name__ == "__main__":
    # it just works
    print(A.myname)
