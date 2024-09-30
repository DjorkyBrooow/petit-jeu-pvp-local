from characters.Class import Class
from characters.classes import *
from game.Square import Square
from game.static.Faction import Faction
import os

class Game:
    
    character_list: list[Class] = []
    alliance_list: list[Class] = []
    horde_list: list[Class]= []
    map: 'Map'
    
    def __init__(self) -> None:
        pass

    def start_game(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""Vous avez lancé une partie de JdR PvP.
Deux équipes vont s'affronter, la première à terrasser l'autre gagne la partie.
Voici les étapes pour commencer la partie :""")
        self.chose_map()
        self.chose_characters()
        character_list = self.alliance_list + self.horde_list
        character_list.sort(key=lambda x: x.priority, reverse=True)
        while self.game_in_progress():
            for character in character_list:
                if character.is_alive:
                    character.play_turn()
            pass

    def chose_map(self) -> None:
        res = False
        while not res:
            width = int(input("1. Choisissez la largeur de la carte (min 10 - max 25): "))
            if width >= 10 and width <= 25:
                res = True
        res = False
        while not res:
            height = int(input("2. Choisissez la hauteur de la carte (min 5 - max 15): "))
            if height >= 5 and height <= 15:
                res = True
        self.map = Map(width, height)
    
    def chose_characters(self) -> None:
        nb_alliance = int(input("3. Choisissez le nombre de personnages de l'Alliance (max 5): "))
        print("4. Choisissez les classes des personnages de l'Alliance")
        print(f"Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}")
        for i in range(nb_alliance):
            res = False
            while not res:
                choice = input(f"Choisissez la classe du personnage {i+1} : ")
                if choice.lower() in [x.lower() for x in Class.AVAILABLE_CLASSES]:
                    class_ = globals()[choice.capitalize()]
                    self.alliance_list.append(class_(Faction.ALLIANCE))
                    res = True
                else:
                    print(f"""Choisissez une classe disponible.
Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}""")
                    
        nb_horde = int(input("5. Choisissez le nombre de personnages de la Horde (max 5): "))
        print("6. Choisissez les classes des personnages de la Horde")
        print(f"Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}")
        for i in range(nb_horde):
            res = False
            while not res:
                choice = input(f"Choisissez la classe du personnage {i+1} : ")
                if choice.lower() in  [x.lower() for x in Class.AVAILABLE_CLASSES]:
                    class_ = globals()[choice.capitalize()]
                    self.horde_list.append(class_(Faction.HORDE))
                    res = True
                else:
                    print(f"""Choisissez une classe disponible.
Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}""")

    def game_in_progress(self) -> bool:
        for elem in self.alliance_list:
            if elem.is_alive():
                return True
        for elem in self.horde_list:
            if elem.is_alive():
                return True    
        return False
    
    def who_is_at_range_ally(self, player: Class) -> list[str]:
        ret = []
        for elem in Game.character_list:
            if elem.faction == player.faction and player.is_at_range(elem):
                ret += elem.content
        return ret
    
    def who_is_at_range_enemy(self, player: Class) -> list[str]:
        ret = []
        for elem in Game.character_list:
            if elem.faction != player.faction and player.is_at_range(elem):
                ret += elem.content
        return ret
    
    def update_map(self) -> None:
        self.map.reset_map()
        for elem in self.character_list:
            self.map.square_list[(elem.x_coord, elem.y_coord)].content = elem.content


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

    def reset_map(self) -> None:
        for i in range(self.width):
            for j in range(self.height):
                self.square_list[(i,j)].reset_content()

    def __str__(self) -> str:
        ret = ""
        for j in range(self.height + 1):
            for i in range(self.width):
                ret += "+---"
            ret += "+\n"
            if j != self.height:
                for i in range(self.width):
                    current_square = self.square_list[(i,j)]
                    ret += f"|{str(current_square)}"
                ret += "|\n"
        return ret
        