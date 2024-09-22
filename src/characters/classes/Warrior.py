from characters.Class import Class
from game.static.Constants import *

class Warrior(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.HIGH_DAMAGE
  range = Range.CLOSE_RANGE
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # Gives 30% chance to reduce the damage taken by half
    # 30% chance to revert a negative effect to the launcher
    super().passive()
    
  def skill_1(self) -> None:
    # Shield bash dealing damage to ennemies in a direction 
    # Blocking damage from this direction for 2 rounds 
    super().skill_1()
  
  def skill_2(self) -> None:
    # The warrior charges an ennemy
    # Immobilizes him
    # Mobility boost for 1 round
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