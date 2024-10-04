from characters.Class import Class
from game.static.Constants import *

class Gravedigger(Class):
  
  max_hp = Health.VERY_HIGH_HP
  mobility = Mobility.VERY_LOW_MOBILITY
  damage = Damage.MID_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 1
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self, faction) -> None:
    super().__init__(faction)

  def passive(self) -> None:
    # Each time a character dies
    # The gravedigger gains permanent damage and max_hp
    # At the beginning of the game
    # A random ennemy character is  designed
    # At the death of this character, the gravedigger doubles the previous bonus
    super().passive()
    
  def skill_1(self) -> None:
    # Hits an ennemy with his shovel
    # Damages are increased if the target is low hp
    super().skill_1()
  
  def skill_2(self) -> None:
    # Targets an area and all characters in this area are immobilized for 1 round
    # Suffering enough damage sets them free
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