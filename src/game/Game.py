from characters.Class import Class
from characters.classes import *
from game.Square import Square
from game.static.Faction import Faction
import os, curses, json

class Game:
    
    character_list: list[Class] = []
    alliance_list: list[Class] = []
    horde_list: list[Class]= []
    map: 'Map'
    data: dict
    nb_alliance: int
    nb_horde: int
    
    def __init__(self) -> None:
        self.data = Game.load_data()
        self.map = Map(self.data["optionsText"][0]["default"], self.data["optionsText"][1]["default"])
        self.nb_alliance = self.data["optionsText"][2]["default"]
        self.nb_horde = self.data["optionsText"][3]["default"]

    def start_game(self) -> None:
        self.chose_characters()
        # self.character_list = self.alliance_list + self.horde_list
        # self.character_list.sort(key=lambda x: x.priority, reverse=True)
        # while self.game_in_progress():
        #     for character in self.character_list:
        #         if character.is_alive:
        #             character.play_turn()
        #     pass
    
    def chose_characters(self) -> None:
        charWidth = len(max(Class.AVAILABLE_CLASSES, key=len))
        charHeight = len(Class.AVAILABLE_CLASSES) + 1
        x = int(round((curses.COLS-1)/2) - round(charWidth/2))
        y = int(round((curses.LINES-1)/2) - round(charHeight/2))
        char_win = curses.newwin(charHeight, charWidth, y, x)
        for i in range (len(Class.AVAILABLE_CLASSES)):
            char_win.addstr(i, 0, Class.AVAILABLE_CLASSES[i])
        char_win.refresh()
        char_win.getch()


#         nb_alliance = int(input("3. Choisissez le nombre de personnages de l'Alliance (max 5): "))
#         print("4. Choisissez les classes des personnages de l'Alliance")
#         print(f"Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}")
#         for i in range(nb_alliance):
#             res = False
#             while not res:
#                 choice = input(f"Choisissez la classe du personnage {i+1} : ")
#                 if choice.lower() in [x.lower() for x in Class.AVAILABLE_CLASSES]:
#                     class_ = globals()[choice.capitalize()]
#                     self.alliance_list.append(class_(Faction.ALLIANCE))
#                     res = True
#                 else:
#                     print(f"""Choisissez une classe disponible.
# Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}""")
                    
#         nb_horde = int(input("5. Choisissez le nombre de personnages de la Horde (max 5): "))
#         print("6. Choisissez les classes des personnages de la Horde")
#         print(f"Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}")
#         for i in range(nb_horde):
#             res = False
#             while not res:
#                 choice = input(f"Choisissez la classe du personnage {i+1} : ")
#                 if choice.lower() in  [x.lower() for x in Class.AVAILABLE_CLASSES]:
#                     class_ = globals()[choice.capitalize()]
#                     self.horde_list.append(class_(Faction.HORDE))
#                     res = True
#                 else:
#                     print(f"""Choisissez une classe disponible.
# Les classes disponibles sont les suivantes : {', '.join(Class.AVAILABLE_CLASSES)}""")

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

    @staticmethod
    def load_data() -> dict:
        #load extradata.json
        basePath = os.path.abspath(os.path.dirname(__file__))
        f = open(basePath+"/extradata.json", encoding="utf-8")
        data = json.load(f)
        f.close()
        return data


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
        