import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

# beer_card = Card('y', 'diamonds')
# print(beer_card)

# deck = FrenchDeck()
# print(deck[0], deck[49], len(deck))

# from random import choice
# print(choice(deck))

# print(deck[:3], deck[12::13]) #  starting on index 12 and skipping 13 cards at a time

# for card in reversed(deck):

# print(Card('QOP', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# for card in sorted(deck, key=spades_high):
#     print(card)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
