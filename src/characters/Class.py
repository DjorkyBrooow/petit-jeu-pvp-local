from game import Game
from game.Square import Square
from game.static.State import State
from game.static.Direction import Direction
from game.Counter import *
from game.static.Faction import Faction
from abc import ABC, abstractmethod
from math import sqrt
from game.static.Constants import Health, Mobility, Damage, Range
import random

class Class(ABC):
    # Common stats
    current_hp: int
    current_mobility: int
    current_damage: int
    current_range: int
    state: State
    is_alive: bool
    critical_rate: float = 0.1
    critical_hit: float = 1.4

    # Unique stats
    max_hp : Health
    mobility: Mobility
    damage: Damage
    range: Range
    direction: Direction
    priority: int
    name: str
    passive_name: str
    passive_description: str
    cooldown_passive: int
    skill_1_name: str
    skill_1_description: str
    cooldown_skill_1: int
    skill_2_name: str
    skill_2_description: str
    cooldown_skill_2: int
    x_coord: int
    y_coord: int
    faction: Faction
    content: str
    id: int = 0

    # Counters
    shield_counters: dict[str: ShieldCounter] = {}
    poison_counters: dict[str: PoisonCounter] = {}
    state_counters: dict[str: StateCounter] = {}
    skill_counters: dict[str: Counter] = {}
    buff_counters: dict[str: Counter] = {}
    counters: list[dict[str: Counter]] = [shield_counters, poison_counters, state_counters, skill_counters, buff_counters]
    
    # Used skills
    
    used_auto_attack: bool = False
    used_skill: bool = False

    # Static variables

    AVAILABLE_CLASSES=[
        'Alchemist',
        'Berserker',
        'Cyborg',
        'Druid',
        'Elementalist',
        'Gravedigger',
        'Hunter',
        'Illusionist',
        'Mage',
        'Necromancer',
        'Oracle',
        'Poisoner',
        'Ranger', 
        'Summoner',
        'Templar',
        'Viking',
        'Warrior',
    ]

    def __init__(self, faction: Faction) -> None:
        self.current_hp = self.max_hp.value
        self.current_mobility = self.mobility.value
        self.current_damage = self.damage.value
        self.current_range = self.range.value
        self.state = State.NORMAL
        self.is_alive = True
        self.faction = faction
        self.name = type(self).__name__ + " " + self.faction.name + " " + str(self.id)
        self.content = self.name[0] + str(self.id) + self.faction.name[0]
        self.direction = Direction.EAST if faction == Faction.ALLIANCE else Direction.WEST
    

    def play_turn(self) -> None:
        pass

    @abstractmethod
    def start_turn(self) -> None:
        pass

    @abstractmethod
    def end_of_turn(self) -> None:
        for poison in self.poison_counters.values():
            self.suffer_damage(self, poison.value)

        for elem in self.counters:
            if len(elem)>0:
                keys_to_remove = []
                for key in elem:
                    counter = elem[key]
                    counter.decrement()
                    if counter.count == 0:
                        keys_to_remove.append(key) 
                    
                for key in keys_to_remove:
                    del elem[key]


        self.used_auto_attack = False
        self.used_skill = False
        
        self.current_mobility = self.mobility.value
        self.current_damage = self.damage.value
        self.current_range = self.range.value
        self.state = State.NORMAL


    @abstractmethod 
    def auto_attack(self, target: 'Class') -> None:
        damage = self.current_damage
        rng = random.randrange(100)
        if rng <= self.critical_rate * 100:
            damage *= self.critical_hit
        target.suffer_damage('Attaque auto', damage)
        self.used_auto_attack = True
    
    @abstractmethod
    def suffer_damage(self, source: str, damage: int) -> None:
        if self.is_alive:
            if self.get_total_shield() > 0:
                diff_shield = damage - self.get_total_shield()
                if diff_shield < 0:
                    shield_list = sorted(self.shield_counters.items(), key=lambda x: (x[1].count, x[1].value))
                    for source_id, shield_counter in shield_list:
                        if shield_counter.value <= diff_shield:
                            self.remove_shield(source_id)
                            diff_shield -= shield_counter.value
                        else:
                            self.shield_counters[source_id].value -= diff_shield
                            break
                        print(f"{self.name} a subi '{damage}' points de dégâts dans le bouclier de {source}")
                else:
                    for id in self.shield_counters.keys():
                        self.remove_shield(id)
                    self.current_hp = self.current_hp - diff_shield
                    print(f"{self.name} a subi {damage} points de '{source}' dont {diff_shield} dans sa barre de PV")

            else:
                self.current_hp = self.current_hp - damage
                print(f"{self.name} a subi {damage} points de '{source}' dans sa barre de PV")
            if self.current_hp <= 0:
                self.current_hp = 0
                self.is_alive = False
        else:
            print("Votre cible n'existe plus")
    
    def heal(self, source: str, value: int) -> None:
        add = self.current_hp + value
        if add <= self.max_hp.value:
            self.current_hp += value

    def __str__(self) -> str:
        return f"{self.content} : {self.current_hp}{f' ({str(self.get_total_shield())})' if self.get_total_shield() > 0 else ''} / {self.max_hp.value}"

    @abstractmethod
    def passive(self) -> None:
        pass

    @abstractmethod
    def skill_1(self, game: Game) -> None:
        self.used_skill = True
        pass

    @abstractmethod
    def skill_2(self, game: Game) -> None:
        self.used_skill = True
        pass

    def move_with_coords(self, x: int, y: int) -> None:
        self.x_coord += x
        self.y_coord += y
        self.current_mobility -= 1
    
    def move_with_direction(self, direction: Direction) -> None:
        if self.current_mobility > 0:
            self.x_coord += direction.value[0]
            self.y_coord += direction.value[1]
            self.current_mobility -= 1
        self.direction = direction
    
    def move_with_str(self, direction: str) -> None:
        if direction == "north":
            self.move_with_direction(Direction.NORTH)
        elif direction == "west":
            self.move_with_direction(Direction.WEST)
        elif direction == "south":
            self.move_with_direction(Direction.SOUTH)
        elif direction == "east":
            self.move_with_direction(Direction.EAST)
            
    
    def is_at_range_character(self, target: 'Class') -> bool:
        res = False
        x_diff= self.x_coord - target.x_coord
        y_diff= self.y_coord - target.y_coord
        distance = sqrt( x_diff**2 + y_diff**2 )
        if distance <= self.current_range:
            res = True
        return res
    
    def is_at_range_coords(self, x: int, y: int) -> bool:
        res = False
        x_diff= self.x_coord - x
        y_diff= self.y_coord - y
        distance = sqrt( x_diff**2 + y_diff**2 )
        if distance <= self.current_range:
            res = True
        return res

    def is_at_range_square(self, square: Square) -> bool:
        res = False
        x_diff= self.x_coord - square.x_coord
        y_diff= self.y_coord - square
        distance = sqrt( x_diff**2 + y_diff**2 )
        if distance <= self.current_range:
            res = True
        return res
    
    def is_ally(self, target: 'Class') -> bool:
        res = False
        if target.team == self.team:
            res = True
        return res
    
    def buff_damage(self, damage_buff: int, duration: int, skill_name: str, target: 'Class') -> bool:
        counter = BuffDamageCounter(damage_buff, skill_name, duration)
        target.buff_counters[skill_name] = counter
        for key in target.buff_counters:
            target.current_damage = target.damage.value + target.buff_counters[key].value
        if target.current_damage < Damage.VERY_LOW_DAMAGE.value:
            target.current_damage = Damage.VERY_LOW_DAMAGE.value
        return True
        
    
    #########################
    #                       #
    #  SHIELDS AND POISONS  #
    #                       #
    #########################

    def add_shield(self, source: str, value: int, duration: int) -> None:
        self.shield_counters[source] = ShieldCounter(value, source, duration)

    def remove_shield(self, source_id: str) -> None:
        if source_id in self.shield_counters:
            del self.shield_counters[source_id]
            print(f"The shield of {source_id} has expired or has been destroyed")
    
    def get_total_shield(self) -> int:
        sum = 0
        for value in self.shield_counters.values():
            sum += value.value
        return sum

    def add_poison(self, source: str, value: int, duration: int) -> None:
        self.shield_counters[source] = PoisonCounter(value, source, duration)

    def remove_poison(self, source_id: str) -> None:
        if source_id in self.poison_counters:
            del self.poison_counters[source_id]
            print(f"The poison of {source_id} has expired or has been cleansed")
    
    def get_total_poison(self) -> int:
        sum = 0
        for value in self.poison_counters.values():
            sum += value.value
        return sum
    
    #########################
    #                       #
    #  GETTERS AND SETTERS  #
    #                       #
    #########################

    def set_coords(self, x: int, y: int) -> None:
        self.x_coord = x
        self.y_coord = y
