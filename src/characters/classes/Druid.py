from characters.Class import Class
from game.static.Constants import *
from game import Game
from enum import Enum


class Form(Enum):
  HUMAN = 0
  BEAR = 1 
  EAGLE = 2
  
class Druid(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.MID_DAMAGE
  range = Range.MID_CLOSE_RANGE
  priority = 11
  cooldown_skill_1 = 1
  cooldown_skill_2 = 3
  current_form = Form.HUMAN
  passive_name = "Changeforme"
  skill_1_name = "Appel de la nature"
  skill_2_name = "Restauration"

  def __init__(self, faction) -> None:
    Druid.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # Each time he changes his form
    # The druid retrieves 2 HP
    # Default form : human
    super().passive()
    
  def skill_1(self, game : Game) -> None:
    # Changes into a bear, an eagle or a human
    # Skill 2 depends on the form
    # Changes stats 
    # Bear : very high hp, low mobility, very low damage, close Range
    # Eagle : very low hp, very high mobility, high damage, mid close range
    if self.current_form == Form.HUMAN:
      self.skill_2_name = "Restauration"
    elif self.current_form == Form.BEAR:
      self.skill_2_name = "Provocation"
    elif self.current_form == Form.EAGLE:
      self.skill_2_name = "Lâcher de rocher"
    super().skill_1(game)
  
  def skill_2(self, game : Game) -> None:
    # Human : Heals a target
    # Bear : Taunts ennemies around him
    # Eagle : Throws a rock from the sky 
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
    
    