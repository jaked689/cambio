from GameData import GameData
from Player import Player

player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

players = [player1, player2, player3, player4]

game = GameData(players, player1._id)

print(game)