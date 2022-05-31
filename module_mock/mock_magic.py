from unittest.mock import MagicMock, Mock


if __name__ == "__main__":
    mock = MagicMock()
    mock.__str__.return_value = "foobarbaz"
    print(str(mock))

    mock.__str__.assert_called_with()

    # use ordinary mock
    mock2 = Mock()
    mock2.__str__ = Mock(return_value="xxxxx")
    print(str(mock2))

    # won't work
    mock2 = Mock()
    mock2.__str__.return_value = "xxxxx"
    print(str(mock2))
