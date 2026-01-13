from characters.Class import Class
from game.static.Constants import *
from game import Game

class Poisoner(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.HIGH_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_CLOSE_RANGE
  priority = 7
  cooldown_skill_1 = 1
  cooldown_skill_2 = 3
  passive_name = ""
  skill_1_name = ""
  skill_2_name = ""

  def __init__(self, faction) -> None:
    Poisoner.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # When the poisoner walks
    # He leaves the case behind him poisonned
    # Lasts 1 round
    # Poisons the ennemy for 2 rounds
    super().passive()
    
  def skill_1(self, game, target: Class) -> None:
    # Launchs a poison on an ennemy target
    # Lasts for 3 rounds 
    super().skill_1(game)
  
  def skill_2(self, game : Game) -> None:
    # Increases his mobility and damage 
    # Lasts 2 rounds
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