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

class Player(object):
    players = []
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.players.append(self)

        # self.play()
    
    def draw(self, deck):
        self.hand.append(deck.draw())
    
    def play(self):
        return self.hand.pop()
    
    def showHand(self):
        for tile in self.hand:
            tile.getSuits()

class gameBoard(object):

    def __init__(self):
        self.round = 1
        self.playArea = []
        self.deal()

    def shuffle(self):
        for i in range(len(self.tiles)-1,0,-1):
            r = random.randint(0, i)
            self.tiles[i], self.tiles[r] = self.tiles[r], self.tiles[i]
    
    def deal(self):
        for i in range(0, len(Player.players)):
            while Player.players[i].hand.__len__() < 12:
                Player.players[i].draw(deck)

            # print(i)
            # Player.players[i].showHand()
            # Player.players[i].draw(deck)
            # print(Player.players[i].hand.__len__())

        



# deck = Deck()
# deck.show()
# deck.shuffle()
# tile = deck.draw()
# tile.getSuits()
# deck.show()

deck = Deck()
gameboard = gameBoard()
deck.shuffle()

print(len(deck.tiles))
bob = Player("Bob")
sue = Player("Sue")
adam = Player("Adam")
print(Player.players)
print (Player.players.__len__())
bob.draw(deck)
bob.draw(deck)
print("bob's tiles")
bob.showHand()
sue.draw(deck)
print("sue's tiles")
sue.showHand()
adam.draw(deck)
print("adam's tiles")
adam.showHand()
print("dealing!!!!!")
gameboard.deal()
print("sue's tiles")
sue.showHand()
print("bob's tiles")
bob.showHand()
print("adam's tiles")
adam.showHand()
print(len(deck.tiles))



