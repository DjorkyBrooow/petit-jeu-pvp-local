from characters.Class import Class
from game.static.Constants import *
from game.Counter import Counter

class Cyborg(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.HIGH_MOBILITY
  damage = Damage.HIGH_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 13
  cooldown_skill_1 = 2
  cooldown_skill_2 = 3
  max_overcharge: int = 5
  current_overcharge: int = 0

  def __init__(self, faction) -> None:
    super().__init__(faction)

  def passive(self) -> None:
    # Can overcharge if too many abilities are used in a short amount of time
    # Overcharge leads to the cyborg being stunned for 1 round
    super().passive()

  def skill_1(self) -> None:
    # Dashes behind a target at Range.MID_LONG_RANGE
    # Deals damage and stuns the target
    # Overcharge += 3
    super().skill_1()
  
  def skill_2(self) -> None:
    # Cleanses all negative effects
    # Heals few hp 
    # Overcharge += 3
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
    # Overcharge -= 1
    super().end_of_turn()
    pass
  
  def suffer_damage(self, source: Class, damage: int) -> None:
    super().suffer_damage(source, damage)