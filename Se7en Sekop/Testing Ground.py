from Card import Card
from Player import Player
from collections import deque
from Table import Table
import random, os

p1 = Player('Dieka')
p2 = Player('Bot 1')
p3 = Player('Bot 2')
p4 = Player('Bot 3')
players = [p1, p2, p3, p4]
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
    players[i].open = deck[i * step: (i + 1) * step]

# Get player with 7 of spades / first turn
starts_from = None
for idx, player in enumerate(players):
    if player.has_7_spade():
        starts_from = idx

player_turns = deque(players)
player_turns.rotate(-starts_from)
_ = os.system("cls")

for n_turns in range(step):
    for player in player_turns:

        if n_turns == 0:
            print "The game starts on " + player.name
            table.put_card(player.draw_card('spade', '7'))
            n_turns += 1
            continue

        table.show()

        print player.name + "'s turn:"
        played_card = player.play(table.get_playable_cards())
        table.put_card(played_card)

        _ = os.system("cls")

        if played_card is not None:
            print player.name + " put " + str(played_card) + " on the table"
        else:
            print player.name + " close a card"

        n_turns += 1

print "the game is finished"
table.show()
game_points = []
for p in players:
    print p.name + " : "
    print str(sorted([str(c) for c in p.closed])) + " --> " + str(p.get_points()) + " total = " + str(sum(p.get_points()))
    print
    game_points.append(p.get_points())

print "the winner is " + players[game_points.index(min(game_points))].name

