from tile import Tile
from deck import Deck
from player import Player

spaces = '    '

deck = Deck()
deck.shuffle()

class Gameboard(object):
    def __init__(self):
        self.numberOfPlayers = 0
        self.numberOfTiles = 15
        self.players = []            # Store the players as a list of Player objects
        self.mexicanTrain = []

    def getPlayers(self):
        while (True):
            self.numberOfPlayers = raw_input("How many people are playing today?\n>")
            self.numberOfPlayers = int(self.numberOfPlayers)
            if (self.numberOfPlayers < 2):
                print("Sorry, this game only supports 2-8 players")
            elif (self.numberOfPlayers <= 4):
                self.numberOfTiles = 15
                break
            elif (self.numberOfPlayers < 7):
                self.numberOfTiles = 12
                break
            elif (self.numberOfPlayers <= 8):
                self.numberOfTiles = 11
                break
            else:
                print("Sorry, this game only supports 2-8 players")

        for i in range(1, int(self.numberOfPlayers)+1):
            name = raw_input("What is player number {}'s name?\n".format(i))
            self.players.append(Player(name))

    def showPlayers(self):
        for i in range (0, len(self.players)):
            print('{}{}'.format(spaces, self.players[i].name))

    def showHands(self):
        for i in range (0, len(self.players)):
            print("{}'s hand").format(self.players[i].name)
            self.players[i].showHand(spaces)
    
    def showTrains(self):
        for i in range (0, len(self.players)):
            print("{}'s train").format(self.players[i].name)
            self.players[i].showTrain(spaces)

    def showMexicanTrain(self, prepend = ''):
        for i, tile in enumerate(self.mexicanTrain, 1):
            print('{}[{}] ({})'.format(prepend, i, tile.getSuitsAsString()))

    def deal(self):
        for i in range (0, len(self.players)):
            for j in range(1, self.numberOfTiles+1):
                self.players[i].draw(deck)

    def findLargestDouble(self):
        largestDouble = Tile(-1,-1)
        playerIndex = None
        tileIndex = None
        while largestDouble.suit1 == -1:
            for i, player in enumerate(self.players):
                for j in range(0,len(player.hand)):
                    if player.hand[j].suit1 == player.hand[j].suit2 and player.hand[j].suit1 > largestDouble.suit1:
                        largestDouble = player.hand[j]
                        playerIndex = i
                        tileIndex = j
            if largestDouble.suit1 == -1:
                for i in range (0, len(self.players)):
                    self.players[i].draw(deck)

        for i, player in enumerate(self.players):
            player.train.append(largestDouble)
        
        self.mexicanTrain.append(largestDouble)
        
        self.players[playerIndex].hand.pop(tileIndex)

        return playerIndex
    
    def gameLoop(self, startingPlayer):
        print('Let\'s start the game!')
        currentPlayer = startingPlayer+1
        availableMoves = {
            'Mexi-Train': self.mexicanTrain[len(self.mexicanTrain)-1].getSuitsAsString(),
            'My-Train': self.players[currentPlayer].showLastTileInTrain()
        }
            
        
        print(availableMoves)

        # "my train" : self.players[currentPlayer].hand[len(hand)-1]
        while True:
            if currentPlayer == len(self.players):
                currentPlayer = 0
            
            print('Player {}\'s hand\n'.format(self.players[currentPlayer].name))
            self.players[currentPlayer].showHand(spaces)
            print('Player {}\'s train\n'.format(self.players[currentPlayer].name))
            self.players[currentPlayer].showTrain(spaces)
            print('Mexican train\n')
            print('{}{}'.format(spaces, self.mexicanTrain[len(self.mexicanTrain)-1].getSuitsAsString()))
            result = raw_input("{}'s turn! If you have a valid tile you can play it on your train or the mexican train otherwise, \
you must draw a tile\n".format(self.players[currentPlayer].name))
            if result == "draw":
                self.players[currentPlayer].draw(deck)
                self.players[currentPlayer].showHand(spaces)
            else:
                tileNum = int(result)-1
                tile = self.players[currentPlayer].hand.pop(tileNum)
                self.players[currentPlayer].train.append(tile)