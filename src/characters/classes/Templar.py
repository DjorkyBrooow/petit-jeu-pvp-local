from characters.Class import Class
from game.static.Constants import *

class Templar(Class):
  
  max_hp = Health.VERY_HIGH_HP
  mobility = Mobility.VERY_LOW_MOBILITY
  damage = Damage.VERY_LOW_DAMAGE
  range = Range.CLOSE_RANGE
  priority = 9
  cooldown_skill_1 = 3
  cooldown_skill_2 = 3
  current_holy_power = 0
  MAX_HOLY_POWER = 5
  passive_name = "Béni par les dieux"
  skill_1_name = "Bénédiction du templier"
  skill_2_name = "Lumière aveuglante"

  def __init__(self, faction) -> None:
    Templar.id += 1
    super().__init__(faction)

  def passive(self) -> None:
    # Stacks holy power when he is hit
    # By an ennemy (not ground effects)
    # Reduces damage taken by ennemies
    # Holy power at max charge is used 
    # To improve the next ability
    super().passive()
    
  def skill_1(self) -> None:
    # Makes himself immune and increases mobility for 1 round
    # Reinforces the next auto attack
    # Buffed : Gives the buff to all allies around him
    super().skill_1()
  
  def skill_2(self) -> None:
    # Creates a blinding light around him
    # That blinds all ennemies while they are in it 
    # Lasts for 3 rounds
    # Buffed : Also heals all allies 
    # And damages ennemies
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