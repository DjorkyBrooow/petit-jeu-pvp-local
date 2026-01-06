from characters.Class import Class
from game.static.Constants import *


class SummonedBeast(Enum):
  NONE = 0
  LYNX = 1 
  RHINO = 2 
  MONKEY = 3

class Hunter(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.HIGH_MOBILITY
  damage = Damage.MID_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 12
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3
  passive_name = ""
  skill_1_name = ""
  skill_2_name = "" 

  def __init__(self, faction) -> None:
    Hunter.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # If the target is alone, deals additional damage
    # If the target is subject to "hunting mark", deals additional damage
    # Both can be cumulated
    super().passive()
    
  def skill_1(self) -> None:
    # Summons a beast to help him fight
    # Only one can be summoned at a time
    # Beast has own abilities
    # Lynx : Hits a target and gives a bleed, additional chances toi crit
    # Rhinoceros : Charge, deals damage to the targets on the way and repells them
    # Monkey : Throws a banana, deals low damage and debuffs the target
    super().skill_1()
  
  def skill_2(self) -> None:
    # Repells the close ennemies in a direction and jumps in the other direction
    super().skill_2()
  
  def start_turn(self) -> None:
    super().start_turn()
  
  
  def auto_attack(self, target: Class) -> None:
    super().auto_attack(target)
    pass
  
  def end_of_turn(self) -> None:
    super().end_of_turn()
    pass
  
  def suffer_damage(self, source: Class, damage: int) -> None:
    super().suffer_damage(source, damage)