from tiles import Tile
from deck import Deck
from players import Player

deck = Deck()
deck.shuffle()
bob = Player("Bob")
sue = Player("Sue")
Adam = Player("Adam")
print(Player.players)
print (Player.players.__len__())
deck.deal()
bob.draw(deck)
bob.showHand()
sue.draw(deck)
sue.showHand()