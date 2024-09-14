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

    def get_type(self) -> SquareType:
        return self.type

    def get_x_coord(self) -> int:
        return self.x_coord

    def get_y_coord(self) -> int:
        return self.y_coord

    def get_player(self) -> bool:
        return self.player

    def get_content(self) -> str:  
        return self.content

    def set_type(self, type: SquareType) -> None:
        self.type = type
    
    def set_x_coord(self, x_coord: int) -> None:
        self.x_coord = x_coord

    def set_y_coord(self, y_coord: int) -> None:
        self.y_coord = y_coord

    def set_player(self, player: bool) -> None:
        self.player = player

    def set_content(self, content: str) -> None:
        self.content = content
        
    def __str__(self) -> str:
        return self.type.value
