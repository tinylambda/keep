import os


if __name__ == '__main__':
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    print(latitude)
    print(longitude)

    x = 100
    y = 200
    x, y = y, x
    print(x, y)

    print(
        divmod(20, 8)
    )

    t = (20, 8)
    print(
        divmod(*t)
    )

    quotient, remainder =  divmod(*t)
    print(quotient)
    print(remainder)

    path = os.path.abspath(__file__)
    _, filename = os.path.split(path)
    print(filename)

