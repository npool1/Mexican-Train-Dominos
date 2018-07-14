class Tile(object):
    def __init__(self, suit1, suit2):
        self.suit1 = suit1
        self.suit2 = suit2

    def getSuits(self):
        print("{} : {}".format(self.suit1, self.suit2))
        # return tuple(suit1, suit2)

    def getPipCount():
        return suit1 + suit2
    
class Deck(object):
    def __init__(self):
        self.tiles = []
        self.build()
        # self.shuffle()

    # Creates a new deck of 12:12 dominoes and shuffles the deck
    def build(self):
        for i in range(0, 13):
            for j in range(i, 13):
                self.tiles.append(Tile(i,j))

    def show(self):
        for t in self.tiles:
            t.getSuits()

deck = Deck()
deck.show()

