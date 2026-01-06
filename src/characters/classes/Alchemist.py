from characters.Class import Class
from game.static.Constants import *
from random import randint
from game import Game

class Alchemist(Class):
  
  max_hp = Health.LOW_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.LOW_DAMAGE
  range = Range.MID_LONG_RANGE
  priority = 10
  cooldown_skill_1 = 1
  cooldown_skill_2 = 4
  passive_name = "Potions incertaines"
  skill_1_name = "Eau de vie"
  skill_2_name = "Feu sacré"

  def __init__(self, faction) -> None:
    Alchemist.id += 1
    super().__init__(faction)
    
  def passive(self, value) -> float:
    # Each target hit by a potion has 25% chance to double its effects 
    rand = randint(1,100)
    if 1<=rand and rand <= 25:
      value = value * 2
    return value

  def skill_1(self, game: Game) -> None:
    # Launches a potion on a target 
    # Can either be a buff on an ally (attack buff)
    # Or a debuff on an ennemy (attack debuff) (cannot be below 1)
    selected_square = game.select_target_square(self, 0, 0)
    target: Class = game.get_character_from_square(selected_square)
    if target is not None:
      if target.faction == self.faction:
        target.buff_damage(self.passive(1), 2, f"{self.skill_1_name} {self.content}", target)
      else:
        target.buff_damage(self.passive(-1), 2, f"{self.skill_1_name} {self.content}", target)
      super().skill_1(game)
  
  def skill_2(self) -> None:
    # Launches a potion on the ground that targets an area
    # All ennemies in the targeted area suffer damages and are burnt for 2 rounds
    # All allies in the targeted area heal for the same amount and heal for 2 rounds
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