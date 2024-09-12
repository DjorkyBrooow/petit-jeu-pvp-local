from game.State import State
from game.Direction import Direction
from game.Counter import Counter
from game.Faction import Faction
from abc import ABC, abstractmethod
from math import sqrt
from game.Constants import Health, Mobility, Damage, Range

class Class(ABC):
    # Base stats
    max_hp : Health
    current_hp: int
    mobility: Mobility
    damage: Damage
    range: Range
    state: State
    direction: Direction
    is_alive: bool
    name: str
    skill_1: str
    cooldown_skill_1: int
    skill_2: str
    cooldown_skill_2: int
    x_coord: int
    y_coord: int
    team: Faction

    # Counters and values
    shield: int
    shield_counter: Counter
    stunned_counter: Counter
    immobilized_counter: Counter
    silence_counter: Counter
    poison: int
    poison_counter: Counter
    cooldown_skill_1_counter: Counter
    cooldown_skill_2_counter: Counter
    counters: dict[str, Counter]

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
        
        self.shield_counter = Counter(0)
        self.stunned_counter = Counter(0)
        self.immobilized_counter = Counter(0)
        self.silence_counter = Counter(0)
        self.counters = {"shield_counter"          : self.shield_counter, 
                        "stunned_counter"          : self.stunned_counter, 
                        "silence_counter"          : self.silence_counter, 
                        "immobilized_counter"      : self.immobilized_counter,
                        "poison_counter"           : self.poison_counter,
                        "cooldown_skill_1_counter" : self.cooldown_skill_1_counter,
                        "cooldown_skill_2_counter" : self.cooldown_skill_2_counter}
        pass

    @abstractmethod
    def end_of_turn(self) -> None:
        for elem in self.counters:
            self.counters[elem].decrement()
        pass

    @abstractmethod 
    def auto_attack(self, target: 'Class') -> None:
        target.suffer_damage(self.damage)
    
    @abstractmethod
    def suffer_damage(self, damage) -> None:
        if self.get_is_alive():
            diff_shield = damage - self.shield
            diff_hp = self.current_hp - diff_shield
            if diff_shield < 0:
                self.set_shield(- diff_shield)
            else:
                self.set_shield(0)
                self.set_shield_counter(0)
                self.set_current_hp(diff_hp)
            if self.current_hp <= 0:
                self.set_is_alive(False)

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

    def get_shield(self) -> int:
        return self.shield
    
    def set_shield(self, shield: int) -> None:
        self.shield = shield

    def get_shield_counter(self) -> Counter:
        return self.shield_counter
    
    def set_shield_counter(self, shield_counter: int) -> None:
        self.shield_counter = Counter(shield_counter)
        self.counters['shield_counter'] = self.shield_counter

    def get_stunned_counter(self) -> Counter:
        return self.stunned_counter
    
    def set_stunned_counter(self, stunned_counter: int) -> None:
        self.stunned_counter = Counter(stunned_counter)
        self.counters['stunned_counter'] = self.stunned_counter

    def get_immobilized_counter(self) -> Counter:
        return self.immobilized_counter
    
    def set_immobilized_counter(self, immobilized_counter: int) -> None:
        self.immobilized_counter = Counter(immobilized_counter)
        self.counters['immobilized_counter'] = self.immobilized_counter

    def get_silence_counter(self) -> Counter:
        return self.silence_counter
    
    def set_silence_counter(self, silence_counter: int) -> None:
        self.silence_counter = Counter(silence_counter)
        self.counters['silence_counter'] = self.silence_counter

    def get_poison_counter(self) -> Counter:
        return self.poison_counter
    
    def set_poison_counter(self, poison_counter: int) -> None:
        self.poison_counter = Counter(poison_counter)
        self.counters['poison_counter'] = self.poison_counter

    def get_cooldown_skill_1_counter(self) -> Counter:
        return self.cooldown_skill_1_counter
    
    def set_cooldown_skill_1_counter(self, cooldown_skill_1_counter: int) -> None:
        self.cooldown_skill_1_counter = Counter(cooldown_skill_1_counter)
        self.counters['cooldown_skill_1_counter'] = self.cooldown_skill_1_counter

    def get_cooldown_skill_2_counter(self) -> Counter:
        return self.cooldown_skill_2_counter
    
    def set_cooldown_skill_2_counter(self, cooldown_skill_2_counter: int) -> None:
        self.cooldown_skill_2_counter = Counter(cooldown_skill_2_counter)
        self.counters['cooldown_skill_2_counter'] = self.cooldown_skill_2_counter

    def get_counters(self) -> list:
        ret = []
        for key in self.counters:
            ret += str(self.counters[key])
        return ret
    