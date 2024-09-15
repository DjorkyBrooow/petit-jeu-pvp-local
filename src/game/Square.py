from game.static.SquareType import SquareType


class Square():
    type: SquareType
    x_coord: int
    y_coord: int
    player: bool = False
    content: str = "   "
    
    def __init__(self, x_coord: int, y_coord: int, type: SquareType = SquareType.EMPTY) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type = type

    def reset_content(self) -> None:
        self.content = "   "
        
    def __str__(self) -> str:
        return self.type.value + self.content + "\033[0m"
