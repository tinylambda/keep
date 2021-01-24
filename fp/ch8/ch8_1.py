class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


if __name__ == '__main__':
    x = Gizmo()
    try:
        y = Gizmo() * 10
    except Exception:
        pass
    print(
        dir()
    )

