from deck import Deck
from tile import Tile
from player import Player

spaces = '    '
print('----------- Testing class \'Player()\' -----------\n')
deck = Deck()

print('Creating player \'Nick\' and player \'Cameron\'')
player1 = Player('Nick')
player2 = Player('Cameron')

print('Draw 5 tiles into Nick\'s hand and Cameron\'s hand...')
for i in range(5):
    player1.draw(deck)

for i in range(5):
    player2.draw(deck)

print('Tiles in Nick\'s hand')
player1.showHand(spaces)

print('Tiles in Cameron\'s hand...')
player2.showHand(spaces)

print('Play the first tile in Nick\'s hand')
print('{}({})'.format(spaces, player1.play(1).getSuits()))
print('Play the last tile in Nick\'s hand')
print('{}({})'.format(spaces, player1.play(4).getSuits()))
print('Tiles in Nick\'s hand')
player1.showHand(spaces)

print('Play the third tile in Cameron\'s hand')
print('{}({})'.format(spaces, player2.play(3).getSuits()))
print('Tiles in Cameron\'s hand...')
player2.showHand(spaces)

