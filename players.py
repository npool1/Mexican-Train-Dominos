from tiles import Tile
from deck import Deck

class Player(object):
    players = []
    def __init__(self, name):
        self.name = name
        Player.players.append(name)
        self.hand = []
        # self.play()
    
    def draw(self, deck):
        self.hand.append(deck.draw())

    def play(self):
        return self.hand.pop()
    
    def showHand(self):
        for tile in self.hand:
            tile.getSuits()


