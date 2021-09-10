

if __name__ == '__main__':
    i = 0

    while True:
        x = i
        v = 2021 * (x ** 2) + 115213 * x - 116290

        if abs(v) == 0:
            break

        x = -i
        v = 2021 * (x ** 2) + 115213 * x - 116290

        if abs(v) == 0:
            break

        i += 1
    print(i)
