from unittest.mock import patch


class RealClass:
    def f(self):
        print("in real f")
        return 10


if __name__ == "__main__":
    with patch.object(RealClass, "f", return_value=None) as mock_method:
        rc = RealClass()
        rc.f(1, 2, 3)

    mock_method.assert_called_with(1, 2, 3)
