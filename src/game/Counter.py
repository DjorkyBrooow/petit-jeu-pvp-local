from game.static.State import State


class Counter:
    skill_source: str
    count: int
    
    def __init__(self, skill_source: str, count: int) -> None:
        self.skill_source = skill_source
        self.count = count

    def decrement(self) -> None:
        if self.count > 0:
            self.count -= 1

    def __str__(self) -> str:
        return f"{self.count}"



class ShieldCounter(Counter):

    value: int

    def __init__(self, value: int, skill_source: str, count: int) -> None:
        self.value = value
        super().__init__(skill_source, count)



class PoisonCounter(Counter):

    value: int

    def __init__(self, value: int, skill_source: str, count: int) -> None:
        self.value = value
        super().__init__(skill_source, count)



class StateCounter(Counter):

    state: State

    def __init__(self, state: State, skill_source: str, count: int) -> None:
        self.state = state
        super().__init__(skill_source, count)
