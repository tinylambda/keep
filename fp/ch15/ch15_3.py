from fp.ch15.ch15_2 import LookingClass


if __name__ == '__main__':
    manager = LookingClass()
    print(manager)

    monster = manager.__enter__()
    print(monster == 'JABBERWOCKY')
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)
