from enum import Enum

class SquareType(Enum):
    EMPTY = "\033[0m"
    FIRE = "\033[41m"
    LAVA = "\033[48;5;130m"
    ICE = "\033[48;5;45m"
    POISON = "\033[48;5;46m"
    WATER = "\033[48;5;21m"
    LIGHT = "\033[48;5;226m"
    SHADOW = "\033[48;5;55m"
    ARCANE = "\033[48;5;135m"



