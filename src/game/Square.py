from game.static.SquareType import SquareType


class Square():
    square_type: SquareType
    square_type_duration: int
    x_coord: int
    y_coord: int
    player_on_square: bool = False
    content: str = "   "
    
    def __init__(self, x_coord: int, y_coord: int, type: SquareType = SquareType.EMPTY) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type = type
        
    def set_square_type(self, square_type: SquareType, duration) -> None:
        self.square_type = square_type
        self.square_type_duration = duration

    def reset_square_type(self) -> None:
        self.type = SquareType.EMPTY

    def reset_content(self) -> None:
        self.content = "   "
        
    def __str__(self) -> str:
        return self.content
