from tile import Tile
from deck import Deck
from player import Player

spaces = '    '
players = []            # Store the players as a list of Player objects

deck = Deck()

players.append(Player("Bob"))
players.append(Player("Sue"))
players.append(Player("Adam"))

print('Player list:')
for _, player in enumerate(players):
    print('{}{}'.format(spaces, player.name))

print('Deal 5 cards into each player\'s hand')
for _, player in enumerate(players):
    for i in range(5):
        player.draw(deck)

print('Display each player\'s hand')
for _, player in enumerate(players):
    print('{}'.format(player.name))
    player.showHand(spaces)