from characters.Class import Class
from game.static.Constants import *

class Alchemist(Class):
  
  max_hp = Health.LOW_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 10
  cooldown_skill_1 = 1
  cooldown_skill_2 = 3

  def __init__(self, faction) -> None:
    Alchemist.id += 1
    super().__init__(faction)
    
  def passive(self) -> None:
    # 
    super().passive()

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
  
  def start_turn(self) -> None:
    super().start_turn()

  def auto_attack(self, target: Class) -> None:
    pass
  
  def move(self) -> None:
    pass
  
  def end_of_turn(self) -> None:
    pass
  
  def suffer_damage(self, source: Class, damage: int) -> None:
    super().suffer_damage(source, damage)