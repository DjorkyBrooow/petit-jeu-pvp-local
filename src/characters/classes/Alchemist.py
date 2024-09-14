from characters.Class import Class
from game.static.Constants import *

class Alchemist(Class):
  
  max_hp = Health.LOW_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  cooldown_skill_1 = 1
  cooldown_skill_2 = 3

  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def skill_1(self) -> None:
    # Launches a potion on a target 
    # Can either be a buff on an ally (attack buff)
    # Or a debuff on an ennemy (attack debuff)
    super().skill_1()
  
  def skill_2(self) -> None:
    # Launches a potion on the ground
    # That lasts for few rounds
    # All ennemies in the targeted area
    # Suffer damages
    super().skill_2()