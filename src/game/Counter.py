from abc import abstractmethod
from game.static.State import State


class Counter():
    skill_source: str
    count: int
    
    def __init__(self, skill_source: str, count: int) -> None:
        self.skill_source = skill_source
        self.count = count

    def decrement(self) -> None:
        if self.count > 0:
            self.count -= 1

    def __str__(self) -> str:
        return f"{self.skill_source} - {self.count} Rounds left"
    
    @abstractmethod
    def reset(self) -> None:
        pass



class ShieldCounter(Counter):

    value: int

    def __init__(self, value: int, skill_source: str, count: int) -> None:
        self.value = value
        super().__init__(skill_source, count)
    
    def reset(self):
        self.value = 0
    
    def __str__(self) -> str:
        res = super().__str__()
        res += f" ({self.value} Shield)"
        return res



class PoisonCounter(Counter):

    value: int

    def __init__(self, value: int, skill_source: str, count: int) -> None:
        self.value = value
        super().__init__(skill_source, count)
    
    def reset(self) -> None:
        self.value = 0
    
    def __str__(self) -> str:
        res = super().__str__()
        res += f" ({self.value} Poison)"
        return res



class StateCounter(Counter):

    state: State

    def __init__(self, state: State, skill_source: str, count: int) -> None:
        self.state = state
        super().__init__(skill_source, count)
    
    def reset(self):
        return super().reset()
    
    def __str__(self):
        res = super().__str__()
        res += f" ({self.state.name} state)"
        return res


class BuffDamageCounter(Counter):

    value: int

    def __init__(self, value: int, skill_source: str, count: int) -> None:
        self.value = value
        super().__init__(skill_source, count)
    
    def reset(self):
        return super().reset()
        
    def __str__(self):
        res = super().__str__()
        res += f" ({self.value} Damage buff)"
        return res