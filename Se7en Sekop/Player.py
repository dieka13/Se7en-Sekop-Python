from Card import Card
from prettytable import PrettyTable


class Player:

    def __init__(self, name):
        self.name = name
        self.open = []
        self.closed = []

    def has_7_spade(self):
        return Card('spade', '7') in self.open

    def draw_card(self, suit, rank):
        del self.open[self.open.index(Card(suit, rank))]
        return Card(suit, rank)

    def close_card(self, card):
        del self.open[self.open.index(card)]
        self.closed.append(card)

    def get_drawable_cards(self, playable_cards):
        drawable_cards = []

        for card in self.open:
            if (card in playable_cards) or (card.rank_string() == '7'):
                drawable_cards.append(card)

        return sorted(drawable_cards)

    def show_hand(self):
        t = PrettyTable()
        suits = [[] for _ in range(len(Card.suits))]

        for card in sorted(self.open):
            suits[card.suit].append(card.rank_string())

        n_max_row = max([len(s) for s in suits])
        for rank in suits:
            for i in range(n_max_row - len(rank)):
                rank.append("")

        for suit, suit_cards in enumerate(suits):
            t.add_column(Card.suits[suit], suit_cards)

        print t

    def get_points(self):
        points = [ card.point for card in self.closed ]

        return points

    def play(self, playable_cards):

        drawable_cards = self.get_drawable_cards(playable_cards)

        print "Your cards : "
        self.show_hand()

        if drawable_cards:
            print "choose card to draw:"
            for c_idx, c in enumerate(drawable_cards):
                print "[" + str(c_idx) + "]", c

            reply = _get_response("(enter card number) : ", [i for i in range(len(drawable_cards))])
            card = drawable_cards[int(reply)]

            return self.draw_card(card.suit, card.rank)

        else:
            print "no playable card, you must close one card"
            print "choose card to close:"
            for c_idx, c in enumerate(sorted(self.open)):
                print "[" + str(c_idx) + "]", c
            reply = _get_response("(enter card number) : ", [i for i in range(len(self.open))])
            card = sorted(self.open)[int(reply)]
            self.close_card(card)

            return None


def _get_response(prompt, valid_options):
    reply = None
    error_message = "please, input a number " + str(valid_options)

    while True:
        try:
            reply = raw_input(prompt)
            reply = int(reply)

            if reply not in valid_options:
                raise ValueError
            else:
                break

        except ValueError:
            print error_message

    return reply
