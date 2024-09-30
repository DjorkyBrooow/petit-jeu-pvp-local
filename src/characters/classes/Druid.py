from characters.Class import Class
from game.static.Constants import *
from enum import Enum


class Form(Enum):
  HUMAN = 0
  BEAR = 1 
  BIRD = 2
  
class Druid(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.MID_DAMAGE
  range = Range.MID_CLOSE_RANGE
  priority = 11
  cooldown_skill_1 = 1
  cooldown_skill_2 = 3
  current_form = Form.HUMAN

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # Each time he changes his format
    # The druid retrieves 2 HP
    # Default form : human
    super().passive()
    
  def skill_1(self) -> None:
    # Changes into a bear, an eagle or a human
    # Skill 2 depends on the form
    # Changes stats 
    # Bear : very high hp, low mobility, very low damage, close Range
    # Eagle : very low hp, very high mobility, high damage, mid close range
    super().skill_1()
  
  def skill_2(self) -> None:
    # Human : Heals a target
    # Bear : Taunts ennemies around him
    # Eagle : Throws a rock from the sky 
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
    
    