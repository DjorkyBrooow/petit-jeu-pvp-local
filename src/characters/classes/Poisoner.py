from characters.Class import Class
from game.static.Constants import *

class Poisoner(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.LOW_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_CLOSE_RANGE
  priority = 7
  cooldown_skill_1 = 1
  cooldown_skill_2 = 3

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # 
    super().passive()
    
  def skill_1(self) -> None:
    # 
    super().skill_1()
  
  def skill_2(self) -> None:
    # 
    super().skill_2()
  
  
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