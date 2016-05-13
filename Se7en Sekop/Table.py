from Card import Card
from prettytable import PrettyTable

class Table:

    def __init__(self):
        self.table = [ [ None for j in range(len(Card.ranks)+1) ] for i in range(len(Card.suits)) ]
        self.closed = [ False for i in range(len(Card.suits)) ]

    def put_card(self, card):
        self.table[card.suit][card.rank] = card

        if(card.rank_string() == 'ace'):
            self.closed[card.suit] = True

    def show(self):
        title = []
        for stat_idx, stat in enumerate(self.closed):
            suit_str = Card.suits[stat_idx]
            if stat:
                suit_str += "(closed)"

            title.append(suit_str)

        t = PrettyTable(title)

        for rank_idx in range(len(self.table[0])):
            row = []

            for suit_idx in range(len(self.table)):
                if self.table[suit_idx][rank_idx] is None:
                    row.append("")
                else:
                    row.append(str(self.table[suit_idx][rank_idx].rank_string()))

            t.add_row(row)

        print t

    def get_putable_cards(self):

        put_cards = []
        for suit_idx, suits in enumerate(self.table):
            for card in suits:
                if (not card is None) and (not self.closed[suit_idx]):
                    put_cards.append(card)

        putable_cards = []
        for card in put_cards:
            if card.rank >= 6:
                putable_cards.append(card.get_upper())

            if card.rank <= 6:
                putable_cards.append(card.get_lower())

        return putable_cards

