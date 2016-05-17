from Card import Card
from Helper import get_response
from prettytable import PrettyTable

class Table:

    def __init__(self):
        self.table = [ [ None for j in range(len(Card.ranks)+1) ] for i in range(len(Card.suits)) ]
        self.closed = [ False for i in range(len(Card.suits)) ]
        self.closed_at = None

    def put_card(self, card):

        if card is not None:
            if card.rank != 0:
                self.table[card.suit][card.rank] = card
            else:
                self.closed[card.suit] = True

                if self.is_closed():

                    if self.closed_at == 'up':
                        self.table[card.suit][len(Card.ranks)] = card
                    elif self.closed_at == 'bottom':
                        self.table[card.suit][card.rank] = card

                else:

                    if self.on_table(Card(card.suit, 'king')) and self.on_table(Card(card.suit, '2')):
                        print 'choose where you want to put ' + str(card) + ' : '
                        print "[0] up"
                        print "[1] bottom"
                        reply = get_response('your choice : ', [0, 1])

                        if reply == 0:
                            self.closed_at = 'up'
                            self.table[card.suit][len(Card.ranks)] = card
                        else:
                            self.closed_at = 'bottom'
                            self.table[card.suit][card.rank] = card

                    elif self.on_table(Card(card.suit, 'king')):
                        self.closed_at = 'up'
                        self.table[card.suit][len(Card.ranks)] = card

                    elif self.on_table(Card(card.suit, '2')):
                        self.closed_at = 'bottom'
                        self.table[card.suit][card.rank] = card

    def show(self):
        title = []
        for stat_idx, stat in enumerate(self.closed):
            suit_str = Card.suits[stat_idx]
            if stat:
                suit_str += "(closed)"

            title.append(suit_str)

        t = PrettyTable(title)

        for rank_idx in sorted(range(len(self.table[0])),reverse=True):
            row = []

            for suit_idx in range(len(self.table)):
                if self.table[suit_idx][rank_idx] is None:
                    row.append("")
                else:
                    row.append(str(self.table[suit_idx][rank_idx].rank_string()))

            t.add_row(row)

        print t

    def get_playable_cards(self):
        put_cards = [[] for i in range(len(Card.suits))]
        playable_cards = []
        
        for suit_idx, suits in enumerate(self.table):
            for card in suits:
                if card is not None:

                    if not self.is_closed():
                        put_cards[card.suit].append(card.rank)

                    elif not self.closed[card.suit]:
                        if (card == Card(card.suit, '2')) or (card == Card(card.suit, 'king')):

                            if (card == Card(card.suit, '2')) and (self.closed_at == 'bottom'):
                                put_cards[card.suit].append(card.rank)
                            elif (card == Card(card.suit, 'king')) and (self.closed_at == 'up'):
                                put_cards[card.suit].append(card.rank)
                        else:
                            put_cards[card.suit].append(card.rank)


        for suit_idx, suit in enumerate(put_cards):
            if suit:
                rank_min = min(suit)
                rank_max = max(suit)
                
                playable_cards.extend([
                    Card(suit_idx, rank_min).lower(), Card(suit_idx, rank_max).higher()
                ])

        return playable_cards

    def on_table(self, card):
        return self.table[card.suit][card.rank] is not None

    def is_closed(self):
        return any(self.closed)
