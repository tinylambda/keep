from unittest.mock import create_autospec


def function(a, b, c):
    pass


mock_function = create_autospec(function, return_value="fishy")
print(mock_function(1, 2, 3))

mock_function.assert_called_with(1, 2, 3)

print(mock_function("wrong arguments"))
