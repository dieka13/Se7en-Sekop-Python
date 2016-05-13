from Card import Card

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_sevens(self):
        pass

    def has_7_spade(self):
        return Card('spade', '7') in self.hand

    def draw_card(self, suit, rank):
        del self.hand[self.hand.index(Card(suit, rank))]
        return Card(suit, rank)

    def close_card(self, suit, rank):
        self.hand[self.hand.index(Card(suit, rank))].close()

    def get_playable_card(self, putable_cards):
        playable_card = []

        for card in self.hand:
            if not card.closed:
                if card in putable_cards or card.rank_string() == '7':
                    playable_card.append(card)

        return playable_card

    def get_points(self):
        points = 0

        for card in self.hand:
            if card.closed:
                points += card.rank

        return points
