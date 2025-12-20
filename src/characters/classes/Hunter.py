from characters.Class import Class
from game.static.Constants import *

class Hunter(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.HIGH_MOBILITY
  damage = Damage.MID_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 12
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3
  passive = ""
  skill_1 = ""
  skill_2 = ""

  def __init__(self, faction) -> None:
    Hunter.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # Deals additionnal damages to distant targets
    super().passive()
    
  def skill_1(self) -> None:
    # Shots a piercing arrow at LONG_RANGE
    # All targets on the way are hit 
    super().skill_1()
  
  def skill_2(self) -> None:
    # Repells the close ennemies in a direction and jumps in the other direction
    super().skill_2()
  
  def start_turn(self) -> None:
    super().start_turn()
  
  
  def auto_attack(self, target: Class) -> None:
    super().auto_attack(target)
    pass
  
  def move(self, x, y) -> None:
    super().move(x, y)
    pass
  
  def end_of_turn(self) -> None:
    super().end_of_turn()
    pass
  
  def suffer_damage(self, source: Class, damage: int) -> None:
    super().suffer_damage(source, damage)