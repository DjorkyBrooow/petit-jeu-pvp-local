from characters.Class import Class
from game.static.Constants import *

class Oracle(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 5
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # Turns the wheel of fate at every launched skill
    # The oracle can never be the target of her own spells 
    # Possibilities :
    # - ALLY
    # Heals an ally 
    # Shields an ally
    # Makes an ally immune
    # Dispells an ally
    # - ENNEMY
    # Deals damage to an ennemy
    # Stuns an ennemy
    # Silences an ennemy
    # Immobilizes an ennemy
    super().passive()
    
  def skill_1(self) -> None:
    # Choice
    # Sacrifies hp to heal all allies
    # Sacrifies hp to damage all ennemies
    super().skill_1()
  
  def skill_2(self) -> None:
    # Heals herself and silences an ally
    # Heals herself and immunizes an ennemy 
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