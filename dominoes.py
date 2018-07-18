import random
class Tile(object):
    def __init__(self, suit1, suit2):
        self.suit1 = suit1
        self.suit2 = suit2

    def getSuits(self):
        print("{} : {}".format(self.suit1, self.suit2))
        # return tuple(self.suit1, self.suit2)

    def getPipCount():
        return suit1 + suit2

class Deck(object):
    def __init__(self):
        self.tiles = []
        self.build()
        self.shuffle()

    # Creates a new deck of 12:12 dominoes and shuffles the deck
    def build(self):
        for i in range(0, 13):
            for j in range(i, 13):
                self.tiles.append(Tile(i,j))

    def show(self):
        for t in self.tiles:
            t.getSuits()
    
    def shuffle(self):
        for i in range(len(self.tiles)-1,0,-1):
            r = random.randint(0, i)
            self.tiles[i], self.tiles[r] = self.tiles[r], self.tiles[i]
    
    def draw(self):
        return self.tiles.pop()

deck = Deck()
# deck.show()
# deck.shuffle()
tile = deck.draw()
tile.getSuits()
# deck.show()


