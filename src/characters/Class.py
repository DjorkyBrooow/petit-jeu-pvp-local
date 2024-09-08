from game.State import State
from game.Direction import Direction
from game.Counter import Counter
from abc import ABC

class Class():
    # Base stats
    max_hp : int
    current_hp: int
    mobility: int
    damage: int
    range: int
    state: State
    direction: Direction
    is_alive: bool
    name: str

    # Counters and values
    shield: int
    shield_counter: Counter
    stunned_counter: Counter
    immobilized_counter: Counter
    silence_counter: Counter
    poison: int
    poison_counter: Counter
    counters: dict[str, Counter]

    # Public variables
    LOW_HP: int = 17
    MID_HP: int = 20
    HIGH_HP: int= 24
    
    LOW_DAMAGE: int = 2
    MID_DAMAGE: int= 3
    HIGH_DAMAGE: int = 4

    LOW_MOBILITY: int = 3
    MID_MOBILITY: int = 4
    HIGH_MOBILITY: int= 5

    CLOSE_RANGE: int = 1
    MID_RANGE: int = 4
    LONG_RANGE: int = 7

    AVAILABLE_CLASSES=[
        'Alchemist',
        'Arcanist',
        'Archer',
        'Bard',
        'Battlemage',
        'Beastmaster',
        'Berserker',
        'Chaman',
        'Cleric',
        'Demon',
        'Demonist',
        'Druid',
        'Elementalist',
        'Enchanter',
        'Executioner',
        'Exorcist',
        'Gladiator',
        'Gravedigger',
        'Hunter',
        'Illusionist',
        'Inquisitor',
        'Mage',
        'Monster',
        'Necromancer',
        'Ninja',
        'Oracle',
        'Outlaw',
        'Paladin',
        'Poisoner',
        'Priest',
        'Ranger',
        'Rogue',
        'Skeleton',
        'Summoner',
        'Templar',
        'Warrior',
        'Wizard'
    ]

    def __init__(self, name: str) -> None:
        self.name = name
        self.max_hp = Class.LOW_HP
        self.current_hp = self.max_hp
        self.shield_counter = Counter(0)
        self.stunned_counter = Counter(0)
        self.immobilized_counter = Counter(0)
        self.silence_counter = Counter(0)
        self.counters = {"shield_counter"     : self.shield_counter, 
                        "stunned_counter"     : self.stunned_counter, 
                        "silence_counter"     : self.silence_counter, 
                        "immobilized_counter" : self.immobilized_counter,
                        "poison_counter"      : self.poison_counter}
        pass

    def end_of_turn(self) -> None:
        for elem in self.counters:
            self.counters[elem].decrement()
        pass
        
    def auto_attack(self, target: 'Class') -> None:
        target.suffer_damage(self.damage)
    
    def suffer_damage(self, damage) -> None:
        if self.is_alive:
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

    def is_alive(self) -> bool:
        return self.is_alive
    
    def set_is_alive(self, is_alive: bool) -> None:
        self.is_alive = is_alive

    def get_max_hp(self) -> int:
        return self.max_hp
    
    def set_max_hp(self, max_hp: int) -> None:
        self.max_hp = max_hp

    def get_current_hp(self) -> int:
        return self.current_hp
    
    def set_current_hp(self, current_hp: int) -> None:
        self.current_hp = current_hp

    def get_mobility(self) -> int:
        return self.mobility
    
    def set_mobility(self, mobility: int) -> None:
        self.mobility = mobility

    def get_damage(self) -> int:
        return self.damage
    
    def set_damage(self, damage: int) -> None:
        self.damage = damage

    def get_range(self) -> int:
        return self.range
    
    def set_range(self, range: int) -> None:
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

    def get_counters(self) -> list:
        ret = []
        for key in self.counters:
            ret += str(self.counters[key])
        return ret
    