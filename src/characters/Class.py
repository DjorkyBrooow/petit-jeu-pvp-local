from game.static.State import State
from game.static.Direction import Direction
from game.Counter import Counter, ShieldCounter, PoisonCounter, StateCounter
from game.static.Faction import Faction
from abc import ABC, abstractmethod
from math import sqrt
from game.static.Constants import Health, Mobility, Damage, Range

class Class(ABC):
    # Common stats
    current_hp: int
    state: State
    is_alive: bool

    # Unique stats
    max_hp : Health
    direction: Direction
    mobility: Mobility
    damage: Damage
    range: Range
    name: str
    skill_1: str
    cooldown_skill_1: int
    skill_2: str
    cooldown_skill_2: int
    x_coord: int
    y_coord: int
    faction: Faction
    content: str

    # Counters and values
    shield_counters: dict[str: ShieldCounter] = {}
    poison_counters: dict[str: PoisonCounter] = {}
    state_counters: dict[str: StateCounter] = {}
    skill_counters: dict[str: Counter] = {}

    # Static variables

    AVAILABLE_CLASSES=[
        'Alchemist', 'Arcanist', 'Archer',
        'Barbarian', 'Bard', 'Battlemage', 'Beastmaster', 'Berserker', 'Blademaster',
        'Chaman', 'Cleric', 'Cyborg',
        'Demon', 'Demonist', 'Druid',
        'Elementalist', 'Enchanter', 'Executioner', 'Exorcist',
        'Gravedigger',
        'Hunter',
        'Illusionist', 'Inquisitor',
        'Monster',
        'Necromancer', 'Ninja',
        'Oracle', 'Outlaw',
        'Paladin', 'Poisoner', 'Priest',
        'Ranger', 'Rogue',
        'Skeleton', 'Sniper', 'Spartan', 'Spy', 'Summoner',
        'Templar',
        'Viking',
        'Warrior', 'Wizard',
    ]

    def __init__(self) -> None:
        self.current_hp = self.max_hp
        self.state = State.NORMAL
        self.is_alive = True
        

    @abstractmethod
    def end_of_turn(self) -> None:
        
        pass
        


    @abstractmethod 
    def auto_attack(self, target: 'Class') -> None:
        target.suffer_damage(self.damage)
    
    @abstractmethod
    def suffer_damage(self, source: 'Class', damage: int) -> None:
        if self.get_is_alive():
            if self.get_total_shield() > 0:
                diff_shield = damage - self.get_total_shield()
                if diff_shield < 0:
                    shield_list = sorted(self.shield_counters.items(), key=lambda x: (x[1].count, x[1].value))
                    for source_id, shield_counter in shield_list:
                        if shield_counter.value <= diff_shield:
                            del self.shield_counters[source_id]
                            diff_shield -= shield_counter.value
                        else:
                            self.shield_counters[source_id].value -= diff_shield
                            break
                else:
                    for id in self.shield_counters.keys():
                        self.remove_shield(id)
                    self.set_current_hp(self.current_hp - diff_shield)
            else:
                self.set_current_hp(self.current_hp - damage)
            if self.current_hp <= 0:
                self.set_is_alive(False)
        else:
            print("Votre cible n'existe plus")

    def __str__(self) -> str:
        return f"{self.name} : {self.current_hp} / {self.max_hp}"

    @abstractmethod
    def skill_1(self) -> None:
        pass

    @abstractmethod
    def skill_2(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:

        pass
    
    def is_at_range(self, target: 'Class') -> bool:
        res = False
        x_diff= self.x_coord - target.x_coord
        y_diff= self.y_coord - target.y_coord
        distance = sqrt( x_diff**2 + y_diff**2 )
        if distance <= self.range:
            res = True
        return res

    def is_ally(self, target: 'Class') -> bool:
        res = False
        if target.team == self.team:
            res = True
        return res
    
    #########################
    #                       #
    #  SHIELDS AND POISONS  #
    #                       #
    #########################

    def add_shield(self, source_id, shield_counter) -> None:
        if source_id in self.shield_counters:
            print("Current shield reset")
        else:
            print(f"Successfully added shield for {shield_counter.count} rounds to block {shield_counter.value} damage")
        self.shield_counters[source_id] = shield_counter

    def remove_shield(self, source_id) -> None:
        if source_id in self.shield_counters:
            del self.shield_counters[source_id]
        print(f"The shield of {source_id} has expired or has been destroyed")
    
    def get_total_shield(self) -> int:
        return sum(self.shield_counters.values())

    def add_poison(self, source_id, poison_counter) -> None:
        if source_id in self.poison_counters:
            print("Current poison reset")
        else:
            print(f"Successfully added poison for {poison_counter.count} rounds to deal {poison_counter.value} damage per round")
        self.poison_counters[source_id] = poison_counter

    def remove_poison(self, source_id) -> None:
        if source_id in self.poison_counters:
            del self.poison_counters[source_id]
        print(f"The poison of {source_id} has expired or has been cleansed")


    def get_total_poison(self) -> int:
        return sum(self.poison_counters.values())

    #########################
    #                       #
    #  GETTERS AND SETTERS  #
    #                       #
    #########################


    def get_is_alive(self) -> bool:
        return self.is_alive
    
    def set_is_alive(self, is_alive: bool) -> None:
        self.is_alive = is_alive

    def get_max_hp(self) -> Health:
        return self.max_hp
    
    def set_max_hp(self, max_hp: Health) -> None:
        self.max_hp = max_hp

    def get_current_hp(self) -> int:
        return self.current_hp
    
    def set_current_hp(self, current_hp: int) -> None:
        self.current_hp = current_hp

    def get_mobility(self) -> Mobility:
        return self.mobility
    
    def set_mobility(self, mobility: Mobility) -> None:
        self.mobility = mobility

    def get_damage(self) -> Damage:
        return self.damage
    
    def set_damage(self, damage: Damage) -> None:
        self.damage = damage

    def get_range(self) -> Range:
        return self.range
    
    def set_range(self, range: Range) -> None:
        self.range = range
    
    def get_state(self) -> State:
        return self.state
    
    def set_state(self, state: State) -> None:
        self.state = state

    def get_direction(self) -> Direction:
        return self.direction
    
    def set_direction(self, direction: Direction) -> None:
        self.direction = direction
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name

    def get_faction(self) -> Faction: 
        return self.faction

    def set_team(self, faction: Faction) -> None:
        self.faction = faction

    def get_cooldown_skill_1(self) -> int:
        return self.cooldown_skill_1

    def set_cooldown_skill_1(self, cooldown_skill_1: int) -> None:
        self.cooldown_skill_1 = cooldown_skill_1