from characters.Class import Class
from game.static.Constants import *

class Berserker(Class):
  
  max_hp = Health.LOW_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.VERY_HIGH_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 17
  cooldown_skill_1 = 4
  cooldown_skill_2 = 2

  def __init__(self, faction) -> None:
    Berserker.id += 1
    super().__init__(faction)
    
  def passive(self) -> None:
    # When hit, increase damage and mobility for 1 round
    super().passive()

  def skill_1(self) -> None:
    # Go into fury mode
    # Increase damage and mobility
    # Increase range
    # Increase damage taken
    # Lasts for 3 rounds
    super().skill_1()
  
  def skill_2(self) -> None:
    # Throws an axe at an ennemy
    # Can be thrown from Range.MID_LONG_RANGE
    super().skill_2()
  
  def start_turn(self) -> None:
    return super().start_turn()

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