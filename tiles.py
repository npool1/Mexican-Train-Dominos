from deck import Deck
from players import Player

class Tile(object):
    def __init__(self, suit1, suit2):
        self.suit1 = suit1
        self.suit2 = suit2

    def getSuits(self):
        print("{} : {}".format(self.suit1, self.suit2))
        # return tuple(self.suit1, self.suit2)

    def getPipCount():
        return suit1 + suit2