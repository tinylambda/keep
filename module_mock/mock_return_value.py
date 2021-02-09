from unittest.mock import MagicMock, Mock


class ProductionClass:
    pass


if __name__ == '__main__':
    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)
    r = thing.method(3, 4, 5, key='value')
    print(r)

    thing.method.assert_called_with(3, 4, 5, key='value')

