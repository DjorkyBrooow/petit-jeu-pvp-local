from characters.Class import Class
from game.static.Constants import *
from game import Game

class Summoner(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.LOW_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.LONG_RANGE
  priority = 2
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3
  passive_name = ""
  skill_1_name = ""
  skill_2_name = ""

  def __init__(self, faction) -> None:
    Summoner.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # Can have only 1 summon at a time 
    # Every buff gets also applied to the summoner 
    # Every summon lasts until they die or they are replaced by the other type
    super().passive()
    
  def skill_1(self, game : Game) -> None:
    # Summons a tiger that deals big damage
    # Other active : Gives venom on the fangs
    # Auto attacks apply poison
    super().skill_1(game)
  
  def skill_2(self, game : Game) -> None:
    # Summons a elephant that can tank big damage
    # Other active : gives a shield 
    # While shield is active, it irradiates and deals damage
    super().skill_2(game)
  
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