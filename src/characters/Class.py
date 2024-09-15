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
    current_mobility: int
    current_damage: int
    state: State
    is_alive: bool

    # Unique stats
    max_hp : Health
    direction: Direction
    mobility: Mobility
    damage: Damage
    range: Range
    priority: int
    name: str
    skill_1: str
    cooldown_skill_1: int
    skill_2: str
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
    counters: list[dict[str: Counter]] = [shield_counters, poison_counters, state_counters, skill_counters]

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
        self.state = State.NORMAL
        self.is_alive = True
        self.faction = faction
        self.name = type(self).__name__ + " " + self.faction.name + " " + str(self.id)
        self.content = self.name[0] + str(self.id) + self.faction.name[0]
    

    def play_turn(self) -> None:
        if self.is_alive:
            self.start_turn()
            self.end_of_turn()
        else:
            pass

    @abstractmethod
    def start_turn(self) -> None:
        if self.state == State.SILENCE:
            self.move(self.x_coord, self.y_coord)
            self.auto_attack()
        elif self.state == State.IMMOBILIZED:
            pass
        elif self.state == State.STUNNED:
            pass
        elif self.state == State.NORMAL:
            pass
        pass

    @abstractmethod
    def end_of_turn(self) -> None:
        for poison in self.poison_counters.values():
            self.suffer_damage(self, poison.value)

        for elem in self.counters:
            for id in elem.keys():
                elem[id].decrement()


    @abstractmethod 
    def auto_attack(self, target: 'Class') -> None:
        target.suffer_damage('Attaque auto', self.damage)
        print (f"{self.name} a lancé 'Attaque auto' sur {target.name}")
    
    @abstractmethod
    def suffer_damage(self, source: str, damage: int) -> None:
        if self.is_alive:
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
                self.is_alive = False
        else:
            print("Votre cible n'existe plus")

    def __str__(self) -> str:
        return f"{self.content} : {self.current_hp}{f' ({str(self.get_total_shield())})' if self.get_total_shield() > 0 else ''} / {self.max_hp.value}"

    @abstractmethod
    def passive(self) -> None:
        pass

    @abstractmethod
    def skill_1(self) -> None:
        pass

    @abstractmethod
    def skill_2(self) -> None:
        pass

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        # if self.x_coord == 0 and coords[0] < 0 or self.y_coord == 0 and coords[1] < 0:
        #     print ("Déplacement impossible hors des limites du terrain")
        # else:
        self.x_coord += x
        self.y_coord += y
        self.current_mobility -= 1
        
            
    
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

    def add_shield(self, shield_counter: ShieldCounter) -> None:
        if shield_counter.skill_source in self.shield_counters:
            print(f"Current shield {shield_counter.skill_source} reset")
        else:
            print(f"Successfully added shield for {shield_counter.count} rounds to block {shield_counter.value} damage")
        self.shield_counters[shield_counter.skill_source] = shield_counter

    def remove_shield(self, source_id: str) -> None:
        if source_id in self.shield_counters:
            del self.shield_counters[source_id]
            print(f"The shield of {source_id} has expired or has been destroyed")
    
    def get_total_shield(self) -> int:
        sum = 0
        for value in self.shield_counters.values():
            sum += value.value
        return sum

    def add_poison(self, poison_counter: PoisonCounter) -> None:
        if poison_counter.skill_source in self.poison_counters:
            print(f"Current poison {poison_counter.skill_source} reset")
        else:
            print(f"Successfully added poison for {poison_counter.count} rounds to deal {poison_counter.value} damage per round")
        self.poison_counters[poison_counter.skill_source] = poison_counter

    def remove_poison(self, source_id: str) -> None:
        if source_id in self.poison_counters:
            del self.poison_counters[source_id]
            print(f"The poison of {source_id} has expired or has been cleansed")


    def get_total_poison(self) -> int:
        return sum(self.poison_counters.values())
