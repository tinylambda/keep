import sys


class RoleMixin:
    def print_name(self):
        print(self.name)


class GameServer(RoleMixin):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    gs = GameServer("GOOD")
    gs.print_name()
