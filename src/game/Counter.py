class Counter:
    
    def __init__(self, value: int) -> None:
        self.value = value

    def decrement(self) -> None:
        if self.value > 0:
            self.value -= 1

    def __str__(self) -> str:
        return f"{self.value}"
