import trio


async def async_double(x):
    return 2 * x


if __name__ == "__main__":
    result = trio.run(async_double, 3)
    print(result)
