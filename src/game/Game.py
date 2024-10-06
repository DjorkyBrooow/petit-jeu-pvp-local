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

    # Instance variables
    all_classes = Class.AVAILABLE_CLASSES
    maxlen = len(max(all_classes, key=len))
    nb_classes = len(all_classes)
    
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
        res = self.chose_characters()
        if not res:
            Game.exit_game(self.stdscr, self.data)
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

        # Window char selection
        charWidth = self.maxlen
        charHeight = self.nb_classes + 1
        x = int(round((curses.COLS-1)/2) - round(charWidth/2))
        y = int(round((curses.LINES-1)/2) - round(charHeight/2))

        while True:
            char_win = curses.newwin(charHeight, charWidth + 2, y, x - 1)
            for i in range (self.nb_classes):
                char_win.addstr(i, int(round((charWidth+2)/2) - round(len(self.all_classes[i])/2)), self.all_classes[i])
            char_win.refresh()

            alliance_text = self.data["choosenAlliance"]
            choice_alliance_win = curses.newwin(2 + self.nb_alliance, len(alliance_text) + 1, 0, 0)
            horde_text = self.data["choosenHorde"]
            choice_horde_win = curses.newwin(2 + self.nb_horde, len(horde_text) + 1, 0, curses.COLS - 1 - len(horde_text))
            index = 0

            # Alliance selection 
            winTitle, index = self.character_selection(
                title = self.data["step1"],
                y_title = y,
                char_win = char_win,
                faction = Faction.ALLIANCE,
                choice_win = choice_alliance_win,
                title_choice = alliance_text,
                index = index,
            )

            if index == -1:
                break
            
            time.sleep(1)
            # Clear screen 
            winTitle.clear()
            char_win.clear()
            winTitle.refresh()
            char_win.refresh()
            time.sleep(0.1)


            for i in range (self.nb_classes):
                char_win.addstr(i, int(round((charWidth+2)/2) - round(len(self.all_classes[i])/2)), self.all_classes[i])
            char_win.chgat(index, 0, curses.A_REVERSE)
            char_win.refresh()

            # Horde selection
            winTitle, index = self.character_selection(
                title = self.data["step2"],
                y_title = y,
                char_win = char_win,
                faction = Faction.HORDE,
                choice_win = choice_horde_win,
                title_choice = horde_text,
                index = index,
            )

            if index == -1:
                break
            
            text = self.data["validateChoice"]
            validate_win = curses.newwin(1, curses.COLS - 1, curses.LINES - 5, 0)
            validate_win.addstr(0, int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
            validate_win.refresh()
            while True:
                key  = validate_win.getkey()
                if key == self.data["yes"] or key == self.data["no"]:
                    break

            if key == self.data["yes"]:
                return True
            elif key == self.data["no"]:
                index = 0
                self.alliance_list = []
                self.horde_list = []
                self.stdscr.clear()
                self.stdscr.refresh()
        return False
    
    def character_selection(
            self, 
            title: str,
            y_title: int,
            char_win: curses.window,
            faction: Faction,
            choice_win: curses.window,
            title_choice: str,
            index: int,
        ) -> None:
        
        # Title window
        xt = int(round((curses.COLS-1)/2) - round(len(title)/2))
        yt = y_title - 3
        winTitle = curses.newwin(2, len(title), yt, xt)
        winTitle.addstr(0, 0, title)
        winTitle.refresh()
        
        choice_win.addstr(0, 0, title_choice+"\n")

        char_win.chgat(index, 0, curses.A_REVERSE)
        nb_choosen = 0
        while nb_choosen < self.nb_alliance:
            key = char_win.getkey()
            if key == 'z':
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == 0:
                    index = self.nb_classes - 1
                else:
                    index -= 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == 's':
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == self.nb_classes - 1:
                    index = 0
                else:
                    index += 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == '\n':
                char = globals()[self.all_classes[index].capitalize()]
                self.alliance_list.append(char(faction))
                if (faction == Faction.ALLIANCE):
                    choice_win.addstr(nb_choosen+2, 0, self.all_classes[index])
                    choice_win.refresh()
                elif (faction == Faction.HORDE):
                    choice_win.addstr(nb_choosen+2, 0, self.all_classes[index])
                    choice_win.refresh()
                nb_choosen += 1
            elif key == self.data["quit"]:
                index = -1
                break
            char_win.refresh()
        return winTitle, index
        


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
    
    @staticmethod
    def exit_game(stdscr, data) -> None:
        stdscr.clear()
        text = data["goodbyeText"]
        text2 = data["goodbyeText2"]
        stdscr.addstr(int(round((curses.LINES-1)/2)), int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
        stdscr.addstr(int(round((curses.LINES-1)/2) + 1), int(round((curses.COLS-1)/2) - round(len(text2)/2)), text2)
        stdscr.refresh()
        time.sleep(2)
        return 


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
        