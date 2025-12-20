from enum import Enum

class State(Enum):
    INVULNERABLE = -3 # Cannot suffer damage nor be affected by effects
    INSENSITIVE = -2 # Cannot suffer damage
    IMMUNE = -1 # Cannot be affected by effects
    NORMAL = 0
    SILENCED = 1 # Cannot cast abilities 
    BLIND = 2 # Cannot cast auto-attacks
    IMMOBILIZED = 3 # Cannot move
    STUNNED = 4  # Cannot play
    
    # Define the specific behavior of the character based on their state