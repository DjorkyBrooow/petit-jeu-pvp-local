from characters.Class import Class
from game.static.Constants import *
from game import Game

class Viking(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.HIGH_MOBILITY
  damage = Damage.HIGH_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 15
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3
  passive_name = ""
  skill_1_name = ""
  skill_2_name = ""

  def __init__(self, faction) -> None:
    Viking.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # The viking gains damage for each ennemy at close range 
    # Gains hp for each ally at close range
    super().passive()
    
  def skill_1(self, game : Game) -> None:
    # Fears all ennemies at close range
    # Increase damage dealt for 3 rounds
    super().skill_1(game)
  
  def skill_2(self, game : Game) -> None:
    # Gains a shield that gives 30% chance to block attacks 
    # For 3 rounds
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