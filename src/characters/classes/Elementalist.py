from characters.Class import Class
from game.static.Constants import *
from enum import Enum


class Element(Enum):
  NO_ELEMENT = 0
  EARTH = 1 
  FIRE = 2 
  AIR = 3 
  WATER = 4

class Elementalist(Class):
  
  max_hp = Health.VERY_LOW_HP
  mobility = Mobility.LOW_MOBILITY
  damage = Damage.VERY_HIGH_DAMAGE
  range = Range.LONG_RANGE
  priority = 4
  cooldown_skill_1 = 2
  cooldown_skill_2 = 5
  current_element: Element = Element.NO_ELEMENT 

  def __init__(self, faction) -> None:
    super().__init__(faction)

  def passive(self) -> None:
    # After changing element
    # the next auto attack
    # casts a specific effect :
    # fire : 2 additionnal damage 
    # water : heals for 2 hp 
    # earth : gives a shield of 2 hp 
    # air : gives 2 additionnal mobility
    super().passive()
    
  def skill_1(self) -> None:
    # Changes current element : 
    # Water, air, fire, earth 
    # Default : no element
    super().skill_1()
  
  def skill_2(self) -> None:
    # Water : launches a water ball that heals all allies in the area, leaves a puddle that heals at each round for 3 rounds
    # Fire : launches a fireball in an area that deals damage to ennemies and leaves flames that deal damage each round for 3 rounds
    # Earth : Gives a shield to all allies around for 1 round
    # Air : Increases mobility of all allies around him for 1 round
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
    
    
