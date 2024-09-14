from enum import Enum

class State(Enum):
    IMMUNE = -1
    NORMAL = 0
    SILENCED = 1
    IMMOBILIZED = 2
    STUNNED = 3
    