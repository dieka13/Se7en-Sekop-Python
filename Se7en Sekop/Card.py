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

    def suit_string(self):
        return Card.suits[self.suit]

    def rank_string(self):
        return Card.ranks[self.rank]

    def __str__(self):
        return self.rank_string() + " of " + self.suit_string()

    def __eq__(self, other):
        return (self.rank == other.rank) and (self.suit == other.suit)

    # Get lower rank card from this card
    def lower(self):
        return Card(self.suit, self.rank-1)

    # Get higher rank card from this card
    def higher(self):
        if self.rank == len(Card.ranks)-1:
            return Card(self.suit, 0)
        else:
            return Card(self.suit, self.rank + 1)
