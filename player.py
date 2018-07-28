from tile import Tile
from deck import Deck

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.draw())

    def play(self, index):
        index -= 1          # Subtract 1 from index so that it is in the range [0, len(hand))
        if index in range(0, len(self.hand)):
            return self.hand.pop(index)
    
    def showHand(self, prepend = ''):
        for i, tile in enumerate(self.hand, 1):
            print('{}[{}] ({})'.format(prepend, i, tile.getSuitsAsString()))
