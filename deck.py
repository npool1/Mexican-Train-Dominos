from tile import Tile
import random

class Deck(object):
    def __init__(self):
        self.tiles = []
        self.build()
        self.shuffle()

    # Creates a new deck of 12:12 dominoes
    def build(self):
        for i in range(0, 13):
            for j in range(i, 13):
                self.tiles.append(Tile(i,j))

    # Shuffles a deck of dominoes
    def shuffle(self):
        for i in range(len(self.tiles)-1, 0, -1):
            r = random.randint(0, i)
            self.tiles[i], self.tiles[r] = self.tiles[r], self.tiles[i]

    def show(self, prepend = ''):
        for t in self.tiles:
            print('{}{}'.format(prepend, t.getSuitsAsString()))
    
    def draw(self):
        if self.tiles:
            return self.tiles.pop()
        else:
            return None

    def size(self):
        return len(self.tiles)