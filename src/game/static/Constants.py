from enum import Enum

class Damage(Enum):
    VERY_LOW_DAMAGE: int = 1
    LOW_DAMAGE: int = 2
    MID_DAMAGE: int= 3
    HIGH_DAMAGE: int = 4
    VERY_HIGH_DAMAGE: int = 5

class Health(Enum):
    VERY_LOW_HP: int = 15
    LOW_HP: int = 17
    MID_HP: int = 20
    HIGH_HP: int= 23
    VERY_HIGH_HP: int = 27
    
class Mobility(Enum):
    VERY_LOW_MOBILITY: int = 2
    LOW_MOBILITY: int = 3
    MID_MOBILITY: int = 4
    HIGH_MOBILITY: int= 5
    VERY_HIGH_MOBILITY: int= 6
    
class Range(Enum):
    CLOSE_RANGE: int = 1
    MID_CLOSE_RANGE: int = 3
    MID_LONG_RANGE: int = 5
    LONG_RANGE: int = 7