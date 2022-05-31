from unittest.mock import patch

from books import fp


@patch("fp.ch1.ch1_1.FrenchDeck")
@patch("fp.ch1.ch1_1.Card")
def test(MockClass1, MockClass2):
    fp.ch1.ch1_1.Card([], [])
    fp.ch1.ch1_1.FrenchDeck()
    assert MockClass1 is fp.ch1.ch1_1.Card
    assert MockClass2 is fp.ch1.ch1_1.FrenchDeck
    # assert MockClass1.called
    # assert MockClass2.called


if __name__ == "__main__":
    test()
