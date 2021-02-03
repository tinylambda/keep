class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


