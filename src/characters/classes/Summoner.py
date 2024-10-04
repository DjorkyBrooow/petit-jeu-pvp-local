from characters.Class import Class
from game.static.Constants import *

class Summoner(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.LOW_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.LONG_RANGE
  priority = 2
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3

  def __init__(self) -> None:
    super().__init__()

  def passive(self) -> None:
    # Can have only 1 summon at a time 
    # Every buff gets also applied to the summoner 
    # Every summon lasts until they die or they are replaced by the other type
    super().passive()
    
  def skill_1(self) -> None:
    # Summons a tiger that deals big damage
    # Other active : Gives venom on the fangs
    # Auto attacks apply poison
    super().skill_1()
  
  def skill_2(self) -> None:
    # Summons a elephant that can tank big damage
    # Other active : gives a shield 
    # While shield is active, it irradiates and deals damage
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