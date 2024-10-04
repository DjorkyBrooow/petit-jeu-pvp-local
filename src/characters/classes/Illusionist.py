from characters.Class import Class
from game.static.Constants import *

class Illusionist(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.LOW_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 3
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # When the illusionist gets below 25% hp 
    # He gets immune for 1 round
    super().passive()
    
  def skill_1(self) -> None:
    # For the next round all damages and effects taken 
    # Will be redirects to the launcher
    # Does not affect damage taken by the ground
    super().skill_1()
  
  def skill_2(self) -> None:
    # The illusionist dashes in an area
    # Deals damage
    # Comes back at his original place at the next round
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