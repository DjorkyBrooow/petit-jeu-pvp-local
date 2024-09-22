from characters.Class import Class
from game.static.Constants import *

class Mage(Class):
  
  max_hp = Health.VERY_LOW_HP
  mobility = Mobility.VERY_LOW_MOBILITY
  damage = Damage.VERY_HIGH_DAMAGE
  range = Range.LONG_RANGE
  priority = 6
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # When the target is stunned
    # The mage deals more damage
    super().passive()
    
  def skill_1(self) -> None:
    # Throws a thunder bolt to an ennemy
    # The target and ennemies at close range 
    # Suffer damage and are stunned
    super().skill_1()
  
  def skill_2(self) -> None:
    # Creates a static field on a line
    # Between the mage and the target (ally or ennemy)
    # All ennemies that cross this line are stunned for 1 round
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