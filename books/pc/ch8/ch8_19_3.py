class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError("not open")

    def write(self, data):
        raise RuntimeError("not open")

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError("already closed")


class OpenConnection(Connection):
    def read(self):
        print("reading")

    def write(self, data):
        print("writing")

    def open(self):
        raise RuntimeError("already open")

    def close(self):
        self.new_state(ClosedConnection)


if __name__ == "__main__":
    c = Connection()
    print(c)

    try:
        c.read()
    except RuntimeError as e:
        print(e)

    c.open()
    print(c)
    c.read()
    c.close()
    print(c)
