from fractions import Fraction
from math import sqrt


def equation(a, b, c, d):
    return (d - b) / (a - c)


def quad(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    print(equation(2, 5, 0, 13))
    print(equation(12, 18, -34, 67))
    v = equation(Fraction(1, 2), Fraction(2, 3), Fraction(1, 5), Fraction(7, 8))

    print(Fraction(1, 2) * v + Fraction(2, 3))
    print(Fraction(1, 5) * v + Fraction(7, 8))

    print(quad(2, 7, -15))
