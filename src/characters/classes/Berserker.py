from characters.Class import Class
from game import Game
from game.Square import Square
from game.static.Constants import *

class Berserker(Class):
  
  max_hp = Health.MID_HP
  mobility = Mobility.MID_MOBILITY
  damage = Damage.VERY_HIGH_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 17
  cooldown_skill_1 = 5
  cooldown_skill_2 = 2
  fury_mode : bool = False
  duration_fury_mode : int = 3
  left_fury_mode : int = 0
  passive_name = "Ce qui ne me tue pas me rend plus fort"
  skill_1_name = "Rage du berserker"
  skill_2_name = "Lancer de hache"
  passive_description = f"""
    When hit, increase damage and mobility for the next round
  """
  skill_1_description = """
    Go into fury mode
    Increase damage and mobility
    Increase range
    Increase damage taken
    Lasts for 3 rounds
  """
  skill_2_description = """
    Throws an axe at an ennemy
    Can be thrown from Range.MID_LONG_RANGE
    Reduces mobility for 2 rounds
  """

  def __init__(self, faction) -> None:
    Berserker.id += 1
    super().__init__(faction)
    
  def passive(self) -> None:
    self.current_mobility += Mobility.VERY_LOW_MOBILITY.value
    self.current_damage += Damage.VERY_LOW_DAMAGE.value
    super().passive()

  def skill_1(self, game: Game) -> None:
    if game.validate_skill_launch():
      if not self.fury_mode:
        self.fury_mode = True
        self.current_damage += int(self.current_damage * 0.3)
        self.current_mobility += int(self.mobility.value * 0.5)
        self.current_range += int(self.range.value)
        self.current_critical_rate += self.base_critical_rate
        self.left_fury_mode = self.duration_fury_mode
        super().skill_1(game)
  
  def skill_2(self, game: Game) -> None:
    selected_square = game.select_ennemy_or_ally_target_square(self, Range.MID_LONG_RANGE, False)
    if isinstance(selected_square, Square):
      target: Class = game.get_character_from_square(selected_square)
      if isinstance(target, Class):
        if target.faction != self.faction:
          target.suffer_damage(self.skill_2_name, int(self.current_damage/2))
        super().skill_2(game)
      else:
        return target
    else:
      return selected_square
  
  def start_turn(self) -> None:
    super().start_turn()

  def auto_attack(self, target: Class) -> None:
    super().auto_attack(target)
    pass
  
  def end_of_turn(self) -> None:
    if self.left_fury_mode > 0:
      self.left_fury_mode -= 1
    elif self.left_fury_mode == 0:
      self.fury_mode = False
    super().end_of_turn()
    pass
  
  def suffer_damage(self, source: Class, damage: int) -> None:
    if self.fury_mode:
      super().suffer_damage(source, int(1.5 * damage))
    else:
      super().suffer_damage(source, damage)