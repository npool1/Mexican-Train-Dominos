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
        # hasDrawn = False
        # firstTurn = True
        # availableMoves = {
        # 'Mexi-Train': self.mexicanTrain[len(self.mexicanTrain)-1].getSuitsAsString(),
        # 'My-Train': self.players[currentPlayer].showLastTileInTrain().getSuitsAsString()
        # }
        
        # print(availableMoves)

        while True:
            if currentPlayer == len(self.players):
                currentPlayer = 0
            
            print('Player {}\'s hand\n'.format(self.players[currentPlayer].name))
            self.players[currentPlayer].showHand(spaces)
            print('Player {}\'s train\n'.format(self.players[currentPlayer].name))
            self.players[currentPlayer].showTrain(spaces)
            print('Mexican train\n')
            print('{}{}'.format(spaces, self.mexicanTrain[len(self.mexicanTrain)-1].getSuitsAsString()))
            action = raw_input("{}'s turn! If you have a valid tile you can play it on your train or the mexican train otherwise, \
    you must draw a tile. First type the name of the train line you would like to play on or type draw to pick up another tile.\n".format(self.players[currentPlayer].name))

            if action == "draw" and self.players[currentPlayer].hasDrawn == False:
                self.players[currentPlayer].draw(deck)
                self.players[currentPlayer].showHand(spaces)
                self.players[currentPlayer].hasDrawn = True
            elif (action == "draw" and hasDrawn == True):
                text = raw_input("Sorry you've already drawn this turn. If you can't make a move type 'done.'")
                if (text == "done"):
                    self.players[currentPlayer].hasDrawn = False
                    self.players[currentPlayer].firstTurn = False
                    currentPlayer += 1
            # allows player to flip tiles in their hand
            elif (action == "flip"):
                whichTile = int(raw_input("Please enter the number of the tile you'd like to flip\n"))
                toFlip = self.players[currentPlayer].hand[whichTile -1].flip()
                self.players[currentPlayer].hand[whichTile-1] = toFlip
            # plays selected tile on mexican train line if selection is valid
            elif (action == "Mexi-Train"):
                whichTile = raw_input("Ok, you selected {}. Now pick the number of the tile you'd like play".format(action))
                tileNum = int(whichTile)-1
                tile = self.players[currentPlayer].hand[tileNum]
                # print(tile.getSuit2())
                self.players[currentPlayer].hand.pop(tileNum)
                value = self.mexicanTrain[len(self.mexicanTrain)-1].getSuit2()
                # print(value)
                if (value == tile.getSuit1()):
                    self.mexicanTrain.append(tile)
                    # self.players[currentPlayer].isOpen = False
                    print("Success!!!!!!")
                    currentPlayer += 1
                else:
                    print("Sorry, that's not a valid move")
                    # self.players[currentPlayer].isOpen = True
            # plays selected tile on players own train line if selection is valid
            elif (action == "My-Train"):
                whichTile = raw_input("Ok, you selected {}. Now pick the number of the tile you'd like play".format(action))
                tileNum = int(whichTile)-1
                tile = self.players[currentPlayer].hand[tileNum]
                print(tile.getSuit2())
                self.players[currentPlayer].hand.pop(tileNum)
                value = self.players[currentPlayer].showLastTileInTrain()
                value = value.getSuit2()
                # value = self.players[currentPlayer].train[len(train)-1].getSuit2()

                print(value)
                if (value == tile.getSuit1()):
                    self.players[currentPlayer].train.append(tile)
                    print("Success!!!!!!")
                    currentPlayer += 1
                else:
                    print("Sorry, that's not a valid move")