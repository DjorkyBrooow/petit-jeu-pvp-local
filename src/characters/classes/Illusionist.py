from characters.Class import Class
from game.static.Constants import *
from game import Game

class Illusionist(Class):
  
  max_hp = Health.HIGH_HP
  mobility = Mobility.LOW_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 3
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3
  passive_name = ""
  skill_1_name = ""
  skill_2_name = ""

  def __init__(self, faction) -> None:
    Illusionist.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # When the illusionist gets below 25% hp 
    # He gets invulnerable for 1 round
    # If damages should kill him for the first time he survives at 1hp
    super().passive()
    
  def skill_1(self, game : Game) -> None:
    # For the next round all damages and effects taken 
    # Will be redirects to the launcher
    # Does not affect damage taken by the ground
    super().skill_1(game)
  
  def skill_2(self, game : Game) -> None:
    # The illusionist dashes in an area
    # Deals damage
    # Comes back at his original place at the start of the next round
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