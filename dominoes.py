class Tile(object):
    def __init__(self, suit1, suit2):
        self.suit1 = suit1
        self.suit2 = suit2

    def getSuits():
        return tuple(suit1, suit2)

    def getPipCount():
        return suit1 + suit2
    
class Dominoes(object):
    def __init__(self):
        self.deck = shuffle()

    # Creates a new deck of 12:12 dominoes and shuffles the deck
    def shuffle(self):
        deck = []
        for i in range(0, 12):
