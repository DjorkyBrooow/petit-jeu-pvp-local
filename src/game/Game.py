from characters.Class import Class
from game.Square import Square

class Game:
    
    character_list: list[Class]
    
    def __init__(self, character_list: list[Class]) -> None:
        self.character_list = character_list
    
    def who_is_at_range_ally(self, player: Class) -> list[Class]:
        ret = []
        for elem in Game.character_list:
            if elem.team == player.team and player.is_at_range(elem):
                ret += elem
        return ret
    
    def who_is_at_range_enemy(self, player: Class) -> list[Class]:
        ret = []
        for elem in Game.character_list:
            if elem.team != player.team and player.is_at_range(elem):
                ret += elem
        return ret


class Map():
    
    width: int
    height: int
    square_list: dict[tuple:'Square'] = {}

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        for i in range(width):
            for j in range(height):
                self.square_list[(i,j)] = Square(i, j)
        pass

    def __str__(self) -> str:
        ret = ""
        for j in range(self.height + 1):
            for i in range(self.width):
                ret += "+---"
            ret += "+\n"
            if j != self.height:
                for i in range(self.width):
                    current_square = self.square_list[(i,j)]
                    ret += f"|{str(current_square)}{current_square.get_content()}\033[0m"
                ret += "|\n"
        return ret
        