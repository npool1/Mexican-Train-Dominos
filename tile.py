class Tile(object):
    def __init__(self, suit1, suit2):
        self.suit1 = suit1
        self.suit2 = suit2

    def getSuits(self):
        return tuple((self.suit1, self.suit2))

    def getSuitsAsString(self):
        return "{} : {}".format(self.suit1, self.suit2)

    def getPipCount(self):
        return self.suit1 + self.suit2