import time
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
    stdscr: curses.window
    
    def __init__(self, stdscr: curses.window) -> None:
        self.data = Game.load_data()
        self.map = Map(self.data["optionsText"][0]["choice"], self.data["optionsText"][1]["choice"])
        self.nb_alliance = self.data["optionsText"][2]["choice"]
        self.nb_horde = self.data["optionsText"][3]["choice"]
        self.stdscr = stdscr

        # COLORS
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        WHITE_ON_BLACK = curses.color_pair(1)
        BLACK_ON_WHITE = curses.color_pair(2)

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
        self.stdscr.clear()
        self.stdscr.refresh()

        all_classes = Class.AVAILABLE_CLASSES
        maxlen = len(max(all_classes, key=len))
        nb_classes = len(all_classes)

        # Window char selection
        charWidth = maxlen
        charHeight = nb_classes + 1
        x = int(round((curses.COLS-1)/2) - round(charWidth/2))
        y = int(round((curses.LINES-1)/2) - round(charHeight/2))
        char_win = curses.newwin(charHeight, charWidth + 2, y, x - 1)
        for i in range (nb_classes):
            char_win.addstr(i, int(round((charWidth+2)/2) - round(len(all_classes[i])/2)), all_classes[i])

        # Alliance selection 
        title = self.data["step1"]
        xt = int(round((curses.COLS-1)/2) - round(len(title)/2))
        yt = y - 3
        winTitle = curses.newwin(2, len(title), yt, xt)
        winTitle.addstr(0, 0, title)

        char_win.refresh()
        winTitle.refresh()
        
        index = 0
        char_win.chgat(index, 0, curses.A_REVERSE)
        nb_alliance_choosen = 0
        while nb_alliance_choosen < self.nb_alliance:
            key = char_win.getkey()
            if key == 'z' or key == curses.KEY_UP:
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == 0:
                    index = nb_classes - 1
                else:
                    index -= 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == 's' or key == curses.KEY_DOWN:
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == nb_classes - 1:
                    index = 0
                else:
                    index += 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == '\n' or key == 'PADENTER':
                char = globals()[all_classes[index].capitalize()]
                self.alliance_list.append(char(Faction.ALLIANCE))
                nb_alliance_choosen += 1
                text = 'Choosen class : ' + all_classes[index]
                choice_win = curses.newwin(1, len(text) + 1, y - 2, int(round((curses.COLS-1)/2) - round(len(text)/2)))
                choice_win.addstr(0, 0, text)
                choice_win.refresh()
            char_win.refresh()
        
        time.sleep(1)
        # Clear screen 
        winTitle.clear()
        choice_win.clear()
        char_win.clear()

        winTitle.refresh()
        choice_win.refresh()
        char_win.refresh()
        
        time.sleep(0.5)

        # Horde selection
        for i in range (nb_classes):
            char_win.addstr(i, int(round((charWidth+2)/2) - round(len(all_classes[i])/2)), all_classes[i])
        char_win.chgat(index, 0, curses.A_REVERSE)
        
        title = self.data["step2"]
        xt = int(round((curses.COLS-1)/2) - round(len(title)/2))
        yt = y - 3
        winTitle.addstr(0, 0, title)

        char_win.refresh()
        winTitle.refresh()

        nb_horde_choosen = 0
        while nb_horde_choosen < self.nb_horde:
            key = char_win.getkey()
            if key == 'z' or key == curses.KEY_UP:
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == 0:
                    index = nb_classes - 1
                else:
                    index -= 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == 's' or key == curses.KEY_DOWN:
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == nb_classes - 1:
                    index = 0
                else:
                    index += 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == '\n' or key == 'PADENTER':
                char = globals()[all_classes[index].capitalize()]
                self.horde_list.append(char(Faction.HORDE))
                nb_horde_choosen += 1
                text = 'Classe choisie : ' + all_classes[index]
                choice_win = curses.newwin(1, len(text) + 1, y - 2, int(round((curses.COLS-1)/2) - round(len(text)/2)))
                choice_win.clear()
                choice_win.addstr(0, 0, text)
                choice_win.refresh()
        
            char_win.refresh()
        
        newwin = curses.newwin(curses.LINES -1, curses.COLS-1, 0, 0)
        newwin.clear()
        newwin.addstr(0, 0, "Vos personnages sont pour l'alliance:")
        for i in range(len(self.alliance_list)):
            newwin.addstr(i+1, 0, f"{i+1}. {self.alliance_list[i]}")
        newwin.addstr(len(self.alliance_list)+1, 0, "Vos personnages sont pour la horde:")
        for i in range(len(self.horde_list)):
            newwin.addstr(i+len(self.alliance_list)+2, 0, f"{i+1}. {self.horde_list[i]}")
        newwin.refresh()
        newwin.getch()


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
        