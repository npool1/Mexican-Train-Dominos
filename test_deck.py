from deck import Deck
from tile import Tile

spaces = '    '
print('----------- Testing class \'Deck()\' -----------\n')
deck = Deck()

print('There are {} tiles in the deck'.format(deck.size()))
print('Calling deck.show()...')
deck.show(prepend = spaces)

print('Reshuffling the deck with deck.shuffle()')
deck.shuffle()

print('There are {} tiles in the deck'.format(deck.size()))
print('Calling deck.show()...')
print('{}>>> Note that result should be different <<<'.format(spaces))
print('{}>>> from previous call to deck.show()    <<<'.format(spaces))
deck.show(prepend = spaces)

print('Drawing 5 tiles from the deck into my hand...')
hand = []
for _ in range(5):
    hand.append(deck.draw())

print('Output the tiles in my hand using tile.getSuitsAsString():')
for _, tile in enumerate(hand):
    print('{}{}'.format(spaces, tile.getSuitsAsString()))

print('Output the tiles in my hand using tile.getSuits():')
for _, tile in enumerate(hand):
    print('{}{}'.format(spaces, tile.getSuits()))         # Convert the tuple to a string

print('Output the pip count for each tile in my hand using tile.getPipCount():')
for _, tile in enumerate(hand):
    print('{}{}'.format(spaces, str(tile.getPipCount())))

print('There are {} tiles in the deck'.format(deck.size()))
print('Calling deck.show()...')
deck.show(prepend = spaces)

print('Call deck.draw() until we draw all of the tiles from the deck...')
for i in range(deck.size() + 1):    # Test that we can draw from an empty deck (should return None)
    tile = deck.draw()
    if tile:                        # Draw from empty deck returns None, check that we have a valid tile before calling getSuits()
        tile.getSuitsAsString()
    else:
        print('Draw from empty deck returned None')

print('----------- Tests completed -----------')