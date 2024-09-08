import State
import Direction
from typing import Final
from abc import ABC

class Class(ABC):
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
    shield_counter: int
    shield: int
    stunned_counter: int
    immobilized_counter: int
    silence_counter: int

    # Public variables
    LOW_HP: Final = 13
    MID_HP: Final = 16
    HIGH_HP: Final= 20
    
    LOW_DAMAGE: Final = 1
    MID_DAMAGE: Final= 2
    HIGH_DAMAGE: Final = 3

    LOW_MOBILITY: Final = 3
    MID_MOBILITY: Final = 4
    HIGH_MOBILITY: Final= 5

    CLOSE_RANGE: Final = 1
    MID_RANGE: Final = 4
    LONG_RANGE: Final = 7


    def end_of_turn(self) -> None:
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

    def get_shield_counter(self) -> int:
        return self.shield_counter
    
    def set_shield_counter(self, shield_counter: int) -> None:
        self.shield_counter = shield_counter