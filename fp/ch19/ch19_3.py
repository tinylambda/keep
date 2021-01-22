from ch19_2 import FrozenJson


if __name__ == '__main__':
    grad = FrozenJson({'name': 'Felix', 'class': 1982})
    print(grad.class_)
    print(
        getattr(grad, 'class')
    )


