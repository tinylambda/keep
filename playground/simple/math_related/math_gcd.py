def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print(gcd(1, 2))
    print(gcd(10, 2))
    print(gcd(10, 5))
    print(gcd(20, 10))
