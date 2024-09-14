
from game.Counter import ShieldCounter
from game.Game import Game, Map
from characters.Class import Class
from game.static.SquareType import SquareType


characters = Class.AVAILABLE_CLASSES

map = Map(10,5)

character_list = []


images = {}
for elem in characters:
  images[elem] = f"ressources/img/characters/{elem}.jpeg"

