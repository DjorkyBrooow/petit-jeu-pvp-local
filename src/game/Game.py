from characters.Class import Class

class Game:
    
    character_list: list[Class]
    
    def __init__(self) -> None:
        pass
    
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


