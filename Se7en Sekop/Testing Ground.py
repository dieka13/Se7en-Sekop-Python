from Card import Card
from Player import Player
from collections import deque
from Table import Table
import random, os

p1 = Player('Dieka')
p2 = Player('Bot 1')
p3 = Player('Bot 2')
p4 = Player('Bot 3')
players = [ p1, p2, p3, p4 ]
table = Table()

# initialize card
deck = []
for i in range(4):
    for j in range(13):
        deck.append(Card(i, j))

random.shuffle(deck)

# deal cards
step = len(deck) // 4
for i in range(4):
    players[i].hand = deck[i * step: (i+1) * step]


# show cards and get player with first turn
starts_from = None
for idx, player in enumerate(players):
    # for card in player.hand:
    #     print str(card) + ",",
    # print

    if player.has_7_spade():
        starts_from = idx

player_turns = deque(players)
player_turns.rotate(-starts_from)


for n_turns in range(step):
    for player in player_turns:

        if n_turns == 0:
            print "The game starts on " + player.name
            table.put_card(player.draw_card('spade', '7'))
            n_turns += 1
            continue

        table.show()

        print player.name + "'s turn:"
        playable_cards = player.get_playable_card(table.get_putable_cards())

        if playable_cards:
            print "choose card to draw:"
            for c_idx, c in enumerate(playable_cards):
                print "["+str(c_idx)+"]", c

            reply = raw_input("(enter card number) : ")
            card = playable_cards[int(reply)]
            table.put_card(player.draw_card(card.suit, card.rank))

            print player.name + " put " + str(card) + " on the table "

        else:
            print "no playable card, you must close one card"
            print "choose card to close:"
            for c_idx, c in enumerate(sorted(player.hand)):
                print "[" + str(c_idx) + "]", c
            reply = raw_input("(enter card number) : ")
            card = sorted(player.hand)[int(reply)]
            player.close_card(card.suit, card.rank)
            print player.name + " close a card"

        n_turns += 10


print "the game is finished"
for p in players:
    print p.name + " : " + str([ str(c) for c in p.hand]) + " --> " + str(p.get_points())
