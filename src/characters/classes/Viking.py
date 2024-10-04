from characters.Class import Class
from game.static.Constants import *

class Viking(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.HIGH_MOBILITY
  damage = Damage.HIGH_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 14
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self, faction) -> None:
    super().__init__(faction)

  def passive(self) -> None:
    # The viking gains damage for each ennemy at close range 
    # Gains hp for each ally at close range
    super().passive()
    
  def skill_1(self) -> None:
    # Fears all ennemies at close range
    # Increase damage dealt for 3 rounds
    super().skill_1()
  
  def skill_2(self) -> None:
    # Gains a shield that gives 30% chance to block attacks 
    # For 3 rounds
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