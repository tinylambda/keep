import collections


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    beer_card = Card("7", "diamonds")
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[0], deck[-1])

    print(deck[:3])
    print(deck[12::13])

    for card in deck:  # doctest: +ELLIPSIS
        print(card)

    r = Card("Q", "hearts") in deck
    print(r)

    r = Card("7", "beast") in deck
    print(r)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card: Card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)
