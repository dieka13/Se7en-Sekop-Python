from Card import Card
from Player import Player, AiPlayer
from collections import deque
from Table import Table
from prettytable import PrettyTable
import random
import os


p1 = Player('Dieka')
p2 = AiPlayer()
p3 = AiPlayer()
p4 = AiPlayer()
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

name = raw_input("Write your name : ")
p1.name = name

for n_turns in range(step):
    for player in player_turns:

        if n_turns == 0:
            print "The game starts on " + player.name
            table.put_card(player.draw_card('spade', '7'))
            n_turns += 1
            continue

        print
        if not isinstance(player, AiPlayer):
            table.show()

            print "-----" + player.name + "'s turn------"
            print

        played_card = player.play(table.get_playable_cards())
        table.put_card(played_card)

        if not isinstance(player, AiPlayer):
            _ = os.system("cls")

        if played_card is not None:
            print player.name + " put " + str(played_card) + " on the table"
        else:
            print player.name + " close a card"

        n_turns += 1

print "the game is finished"
table.show()

print "scoreboard : "
t = PrettyTable()
game_points = []
closed_cards = []

for p in players:
    game_points.append(p.get_points(table.is_closed(), table.closed_at))
    closed_cards.append(p.closed)

n_rows = [ len(closed) for closed in closed_cards ]
max_n_rows = max(n_rows)
for closed in closed_cards:
    for i in range(max_n_rows - len(closed)):
        closed.append("")

for p_idx, closed in enumerate(closed_cards):
    t.add_column(players[p_idx].name, closed)

print t
print "the loser is " + players[game_points.index(max(game_points))].name

