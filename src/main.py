
from game.Counter import ShieldCounter
from game.Game import Game, Map
from characters.Class import Class
from characters.classes.Alchemist import Alchemist
from game.static.SquareType import SquareType


characters = Class.AVAILABLE_CLASSES

map = Map(10,5)

char = Alchemist()
print (char.name)

character_list = []


images = {}
for elem in characters:
  images[elem] = f"ressources/img/characters/{elem}.jpeg"
