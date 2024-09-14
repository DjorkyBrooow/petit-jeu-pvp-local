
from game.Game import Game
from characters.Class import Class


characters = Class.AVAILABLE_CLASSES
SQUARE_SIZE: int = 50
MAP_WIDTH: int = 640
MAP_HEIGHT: int = 480

images = {}
for elem in characters:
  images[elem] = f"ressources/img/characters/{elem}.jpeg"

