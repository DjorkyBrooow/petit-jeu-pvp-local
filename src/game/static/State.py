from enum import Enum

class State(Enum):
    IMMUNE = -1
    NORMAL = 0
    SILENCED = 1
    BLIND = 2
    IMMOBILIZED = 3
    STUNNED = 4
    
    # Define the specific behavior of the character based on their state