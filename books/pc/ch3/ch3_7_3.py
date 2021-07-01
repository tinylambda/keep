import math

if __name__ == '__main__':
    a = float('inf')
    print(a + 45)
    print(a * 10)
    print(10 / a)

    a = float('inf')
    print(a/a)

    b = float('-inf')
    print(a + b)

    c = float('nan')
    print(c + 23)
    print(c / 2)
    print(c * 2)
    print(math.sqrt(c))

    d = float('nan')
    print(c == d)
    print(c is d)

    a2 = float('inf')
    print(a == a2)
    print(a is a2)

