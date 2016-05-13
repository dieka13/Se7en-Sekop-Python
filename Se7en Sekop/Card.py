class Card:

    suits = ('heart', 'spade', 'diamonds', 'clubs')
    ranks = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')

    def __init__(self, suit, rank):
        if isinstance(suit, basestring):
            self.suit = Card.suits.index(suit)
        else:
            self.suit = suit

        if isinstance(rank, basestring):
            self.rank = Card.ranks.index(rank)
        else:
            self.rank = rank

        self.closed = False

    def suit_string(self):
        return Card.suits[self.suit]

    def rank_string(self):
        return Card.ranks[self.rank]

    def __str__(self):
        return self.rank_string() + " of " + self.suit_string()

    def __eq__(self, other):
        return (self.rank == other.rank) and (self.suit == other.suit)

    def close(self):
        self.closed = True

    def get_lower(self):
        if self.rank == 0:
            return Card(self.suit, len(Card.ranks)-1)
        else:
            return Card(self.suit, self.rank-1)

    def get_upper(self):
        if self.rank == len(Card.ranks):
            return Card(self.suit, 0)
        else:
            return Card(self.suit, self.rank + 1)
