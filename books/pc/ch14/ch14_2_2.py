from unittest.mock import patch

from books.pc.ch14 import mymodule


@patch("books.pc.ch14.mymodule.func2")
def test1(mock_func):
    mymodule.func2("x")
    mock_func.assert_called()
    mock_func.assert_called_with("x")


def test11():
    with patch("books.pc.ch14.mymodule.func1") as mock_func:
        mymodule.func1()
        print(mock_func is mymodule.func1)
        mock_func.assert_called()


def test111():
    p = patch("books.pc.ch14.mymodule.func2")
    mock_func = p.start()
    mymodule.func2("hello")
    mock_func.assert_called_with("hello")
    p.stop()


@patch("books.pc.ch14.mymodule.func0")
@patch("books.pc.ch14.mymodule.func1")
@patch("books.pc.ch14.mymodule.func2")
def test2(mock2, mock1, mock0):
    mymodule.func0()
    mymodule.func1()
    mymodule.func2("hello")

    mock0.assert_called()
    mock1.assert_called()
    mock2.assert_called()
    mock2.assert_called_with("hello")


def test3():
    with patch("books.pc.ch14.mymodule.func0") as mock0, patch(
        "books.pc.ch14.mymodule.func1"
    ) as mock1, patch("books.pc.ch14.mymodule.func2") as mock2:
        mymodule.func0()
        mymodule.func1()
        mock0.assert_called()
        mock1.assert_called()
        mymodule.func2("y")
        mock2.assert_called_with("y")


# pytest books/pc/ch14/ch14_1_4.py
