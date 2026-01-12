from enum import Enum
from game.static.Constants import Damage

class SquareType(Enum):
    EMPTY = 0
    FIRE = 1
    LAVA = 2
    ICE = 3
    POISON = 4
    WATER = 5
    LIGHT = 6
    SHADOW = 7
    ARCANE = 8
    HOLY_FIRE = 9
    
    def __str__(self) -> str:
        return self.name



