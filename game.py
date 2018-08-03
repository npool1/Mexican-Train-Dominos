from tile import Tile
from deck import Deck
from player import Player
from gameBoard import Gameboard

def main():
    gameboard = Gameboard()

    spaces = '    '

    print("Welcome to Mexican-Train-Dominos!")

    gameboard.getPlayers()

    print("Let's get started. We'll shuffle up the tiles and deal you each {} tiles\n".format(gameboard.numberOfTiles))

    gameboard.deal()

    print("Here's everybody's hand")

    gameboard.showHands()

    startingPlayer = gameboard.findLargestDouble()

    gameboard.showTrains()

    gameboard.showHands()

    gameboard.gameLoop(startingPlayer)




    # for i in range (0, len(gameboard.players)):      
    #     print('Tiles in {} hand' .format(player[i].name + "'s"))
    #     gameboard.player[i].showHand(spaces)

    # print('Tiles in {} hand' .format(player2.name + "'s"))
    # player1.showHand(spaces)

    # print(gameboard.checksForDoubles())

if __name__ == '__main__':
    main()