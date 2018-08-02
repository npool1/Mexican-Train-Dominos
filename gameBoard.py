from tile import Tile
from deck import Deck
from player import Player

spaces = '    '

class Gameboard(object):
    def __init__(self):
        self.numberOfPlayers = 0
        self.numberOfTiles = 15
        self.players = []            # Store the players as a list of Player objects


# print('Player list:')
# for _, player in enumerate(players):
#     print('{}{}'.format(spaces, player.name))

# print('Deal 5 cards into each player\'s hand')
# for _, player in enumerate(players):
#     for i in range(5):
#         player.draw(deck)

# print('Display each player\'s hand')
# for _, player in enumerate(players):
#     print('{}'.format(player.name))
#     player.showHand(spaces)
    def getPlayers(self):
        self.numberOfPlayers = raw_input("How many people are playing today?\n>")
        self.numberOfPlayers = int(self.numberOfPlayers)

        for i in range(1, int(self.numberOfPlayers)+1):
            name = raw_input("What is player number {}'s name?\n".format(i))
            self.players.append(Player(name))

        if (self.numberOfPlayers <= 4):
            self.numberOfTiles = 15
        elif (numberOfPlayers < 7):
            self.numberOfTiles = 12
        else:
            self.numberOfTiles = 11

    def showPlayers(self):
        for i in range (0, len(self.players)):
            print('{}{}'.format(spaces, self.players[i].name))

    def showHands(self):
        for i in range (0, len(self.players)):
            print("{}'s hand").format(self.players[i].name)
            self.players[i].showHand(spaces)

    def checksForDoubles(self):
        doubles = []
        for player in players:
            for i in range(0,len(player.hand)):
                if tile.suit1 == tile.suit2:
                    doubles.append(tile)
        return doubles 