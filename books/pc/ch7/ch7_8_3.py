import math

from functools import partial

points = [(1, 2), (3, 4), (5, 7), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)


if __name__ == '__main__':
    pt = (4, 3)
    points.sort(key=partial(distance, pt))
    print(points)

