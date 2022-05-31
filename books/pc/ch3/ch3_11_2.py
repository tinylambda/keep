import random


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]
    print([random.choice(values) for _ in range(5)])
    print([random.sample(values, 2) for _ in range(2)])
    print([random.sample(values, 3) for _ in range(2)])

    print("-" * 64)

    random.shuffle(values)
    print(values)
    random.shuffle(values)
    print(values)

    print("-" * 64)

    print([random.randint(0, 10) for _ in range(6)])
    print([random.random() for _ in range(3)])

    print("-" * 64)

    print(random.getrandbits(200))
