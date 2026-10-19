import os
from src.controllers.game_controller import GameController


if not os.path.exists("logs"):
    os.mkdir("logs")

if not os.path.exists("saves"):
    os.mkdir("saves")

game = GameController(10, 10)
game.run()
