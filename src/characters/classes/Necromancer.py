from characters.Class import Class
from game.static.Constants import *

class Necromancer(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.VERY_LOW_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 8
  cooldown_skill_1 = 5
  cooldown_skill_2 = 4

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # Each time an ennemy dies, he appears again as a living dead
    # He has half of the stats of the original character
    super().passive()
    
  def skill_1(self) -> None:
    # Curses an ennemy and circles him
    # The ennemy is not allowed move for 1 round
    # If he moves he is cursed for the next 3 rounds
    # Increasing the damages he suffers
    super().skill_1()
  
  def skill_2(self) -> None:
    # Suffers damage and gains a damage buff 
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