from main.agent.random_agent import RandomCarcassonneAgent
from main.carcassonne_game import CarcassonneGame
from main.carcassonne_visualiser import CarcassonneVisualiser


visualiser = CarcassonneVisualiser()
player1 = RandomCarcassonneAgent()
player2 = RandomCarcassonneAgent()
game = CarcassonneGame(players=[player1, player2], visualiser=visualiser)
game.play_game()
