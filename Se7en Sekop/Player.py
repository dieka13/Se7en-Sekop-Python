from prettytable import PrettyTable
from random import randint
from Card import Card
from Helper import get_response


class Player(object):

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

    def show_cards(self):
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

    def show_closed_cards(self):
        t = PrettyTable()
        suits = [[] for _ in range(len(Card.suits))]

        for card in sorted(self.closed):
            suits[card.suit].append(card.rank_string())

        n_max_row = max([len(s) for s in suits])
        for rank in suits:
            for i in range(n_max_row - len(rank)):
                rank.append("")

        for suit, suit_cards in enumerate(suits):
            t.add_column(Card.suits[suit], suit_cards)

        print t

    def get_points(self, closed, closed_at):

        points = 0

        for card in self.closed:
            if card.rank != 0:
                points += card.rank+1
            else:
                if closed:
                    if closed_at == 'up':
                        points += 14
                    else:
                        points += 1
                else:
                    points += 7

        return points

    def play(self, playable_cards):
        drawable_cards = self.get_drawable_cards(playable_cards)

        # for c in playable_cards:
        #     print str(c) + ",",
        # print

        print "Closed cards : "
        self.show_closed_cards()
        print

        print "Cards :"
        self.show_cards()
        print

        if drawable_cards:

            print "choose card to draw :"
            for c_idx, c in enumerate(drawable_cards):
                print "[" + str(c_idx) + "]", c

            reply = get_response("(enter card number) : ", [i for i in range(len(drawable_cards))])
            card = drawable_cards[int(reply)]

            return self.draw_card(card.suit, card.rank)

        else:
            print "no playable card, you must close one card"
            print "choose card to close:"
            for c_idx, c in enumerate(sorted(self.open)):
                print "[" + str(c_idx) + "]", c
            reply = get_response("(enter card number) : ", [i for i in range(len(self.open))])
            card = sorted(self.open)[int(reply)]
            self.close_card(card)

            return None


class AiPlayer(Player):
    id = 1

    def __init__(self):
        Player.__init__(self, 'AI BOT ' + str(AiPlayer.id))
        AiPlayer.id += 1

    # random, for now
    def _best_close(self):
        selection = self.open[randint(0, len(self.open)-1)]
        self.close_card(selection)

    # random, for now
    def _best_draw(self, drawable_cards):
        return drawable_cards[randint(0, len(drawable_cards)-1)]

    def play(self, playable_cards):
        drawable_cards = self.get_drawable_cards(playable_cards)

        if drawable_cards:
            return self._best_draw(drawable_cards)
        else:
            self._best_close()
            return None

