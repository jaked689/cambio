from GameData import GameData
from Player import Player
from Enums import Moves

player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

players = [player1, player2]

game = GameData(players, player1._id)

print(game)
while(True):
    player1input = input("Command here: ")
    game.parsePlay(player1._id, Moves.MATCH, int(player1input), 0)
    player1input = input("Command here: ")
    game.parsePlay(player1._id, Moves.MATCH_GIVE_CARD, int(player1input), 0)
    print(game)