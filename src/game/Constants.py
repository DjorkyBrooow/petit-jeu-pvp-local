from enum import Enum


class Damage(Enum):
    LOW_DAMAGE: int = 2
    MID_DAMAGE: int= 3
    HIGH_DAMAGE: int = 4


class Health(Enum):
    LOW_HP: int = 17
    MID_HP: int = 20
    HIGH_HP: int= 24
    
class Mobility(Enum):
    LOW_MOBILITY: int = 3
    MID_MOBILITY: int = 4
    HIGH_MOBILITY: int= 5
    
class Range(Enum):
    CLOSE_RANGE: int = 1
    MID_RANGE: int = 4
    LONG_RANGE: int = 7