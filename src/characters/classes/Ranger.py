from characters.Class import Class
from game.static.Constants import *

class Ranger(Class):
  
  max_hp = Health.LOW_HP
  mobility = Mobility.VERY_HIGH_MOBILITY
  damage = Damage.HIGH_DAMAGE
  range = Range.LONG_RANGE
  priority = 16
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self, faction) -> None:
    super().__init__(faction)

  def passive(self) -> None:
    # The bigger the distance
    # The bigger the damage
    super().passive()
    
  def skill_1(self) -> None:
    # Shoots a perforing shot 
    # Ignores shields and continues behind the target
    super().skill_1()
  
  def skill_2(self) -> None:
    # Executes an ennemy
    # If the target is low hp 
    # Critical hit granted
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