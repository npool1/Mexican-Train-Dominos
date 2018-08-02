from tile import Tile
from deck import Deck
from player import Player
from gameBoard import Gameboard

gameboard = Gameboard()
deck = Deck()
deck.shuffle()
spaces = '    '

print("Welcome to Mexican-Train-Dominos!")

gameboard.getPlayers()

print("Let's get started. We'll shuffle up the tiles and deal you each {} tiles\n".format(gameboard.numberOfTiles))

for i in range (0, len(gameboard.players)):
    for j in range(1, gameboard.numberOfTiles+1):
        gameboard.players[i].draw(deck)

print("Here's everybody's hand")
gameboard.showHands()
# for i in range (0, len(gameboard.players)):
#     print("{}'s hand").format(gameboard.players[i].name)
#     gameboard.players[i].showHand(spaces)

# for i in range (0, len(gameboard.players)):      
#     print('Tiles in {} hand' .format(player[i].name + "'s"))
#     gameboard.player[i].showHand(spaces)

# print('Tiles in {} hand' .format(player2.name + "'s"))
# player1.showHand(spaces)

# print(gameboard.checksForDoubles())