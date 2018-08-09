
from tile import Tile
from deck import Deck

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.train = []
        self.isOpen = False
        self.hasDrawn = False
        self.firstTurn = True
    
    def draw(self, deck):
        self.hand.append(deck.draw())

    def play(self, index):
        index -= 1          # Subtract 1 from index so that it is in the range [0, len(hand))
        if index in range(0, len(self.hand)):
            return self.hand.pop(index)

    def showLastTileInTrain(self, prepend =''):
        lastTile = self.train[len(self.train)-1]
        # return lastTile.getSuitsAsString()
        return lastTile
    def showHand(self, prepend = ''):
        for i, tile in enumerate(self.hand, 1):
            print('{}[{}] ({})'.format(prepend, i, tile.getSuitsAsString()))
    
    def showTrain(self, prepend = ''):
        for i, tile in enumerate(self.train, 1):
            print('{}[{}] ({})'.format(prepend, i, tile.getSuitsAsString()))

    def flipTile(self, index):
        index -= 1          # Subtract 1 from index so that it is in the range [0, len(hand))
        if index in range(0, len(self.hand)):
            print("in flipTile in player.py")
            return self.hand[index].flip()
