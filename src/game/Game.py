import time
from typing import Tuple, Union
from characters.Class import Class
from characters.classes import *
from game.Square import Square
from game.static.Constants import Range
from game.static.Direction import Direction
from game.static.Faction import Faction
import os, curses, json

from game.static.SquareType import SquareType

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
    
    # COLORS
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(8, curses.COLOR_RED, curses.COLOR_WHITE)
    WHITE_ON_BLACK = curses.color_pair(1)
    BLACK_ON_WHITE = curses.color_pair(2)
    BLACK_ON_RED = curses.color_pair(3)
    RED_ON_BLACK = curses.color_pair(4)
    BLACK_ON_BLUE = curses.color_pair(5)
    BLUE_ON_BLACK = curses.color_pair(6)
    WHITE_ON_RED = curses.color_pair(7)
    RED_ON_WHITE = curses.color_pair(8)
    
    # WINDOWS
    map_window: curses.window
    title_window: curses.window = curses.newwin(3, curses.COLS - 1, 2, 0)
    options_window: curses.window = curses.newwin(9, int((curses.COLS - 1)/2), curses.LINES - 10, 10)
    target_window: curses.window = curses.newwin(5, int((curses.COLS - 1)/8), 2, int(7*(curses.COLS - 1)/8))
    character_window: curses.window = curses.newwin(5, int((curses.COLS - 1)/8), 2, int((curses.COLS - 1)/8))
    
    def __init__(self, stdscr: curses.window) -> None:
        self.data = Game.load_data()
        self.map = Map(self.data["optionsText"][0]["choice"], self.data["optionsText"][1]["choice"])
        self.nb_alliance = self.data["optionsText"][2]["choice"]
        self.nb_horde = self.data["optionsText"][3]["choice"]
        self.stdscr = stdscr
        
        mapWidth = 4*self.map.width+1
        mapHeight = 2*self.map.height+2
        x = int(round((curses.COLS-1)/2) - round(mapWidth/2))
        y = int(round((curses.LINES-1)/2) - round(mapHeight/2))
        self.map_window = curses.newwin(mapHeight, mapWidth, y, x)

    def start_game(self) -> bool:
        res = self.chose_characters()
        if not res:
            Game.exit_game(self.stdscr, self.data)
        self.initialize_characters()
        self.update_map()
        
        gameStartText = self.data["gameStart"]
        
        self.display_map(gameStartText)
        round_number = 1
        # self.map_window.border()
        self.map_window.refresh()
        # self.map_window.getch()
        while self.game_in_progress():
            for character in self.character_list:
                if character.is_alive:
                    res = self.play_turn(character, round_number)
                    if not res:
                        return False
            for character in self.character_list:
                if character.is_alive:
                    character.end_of_turn()
            round_number += 1
        return True
    
    def chose_characters(self) -> bool:
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
                faction_list = self.alliance_list,
                nb_faction= self.nb_alliance,
                choice_win = choice_alliance_win,
                title_choice = alliance_text,
                index = index,
            )

            if index == -1:
                break
            
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
                faction_list = self.horde_list,
                nb_faction= self.nb_horde,
                choice_win = choice_horde_win,
                title_choice = horde_text,
                index = index,
            )

            if index == -1:
                break
            
            self.display_options({
                self.data["yes_key"] : self.data["yes_value"],
                self.data["no_key"] : self.data["no_value"],
                self.data["quit_key"] : self.data["quit_value"],
            }, index=5)
            
            text = self.data["validateChoice"]
            validate_win = curses.newwin(1, curses.COLS - 1, curses.LINES - 8, 0)
            validate_win.addstr(0, int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
            validate_win.refresh()
            
            while True:
                key  = validate_win.getkey()
                if key == self.data["quit_key"]:
                    return False
                elif key == self.data["yes_key"] or key == self.data["no_key"]:
                    break

            if key == self.data["yes_key"]:
                self.options_window.clear()
                self.stdscr.clear()
                return True
            elif key == self.data["no_key"]:
                self.options_window.clear()
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
            faction_list: list,
            nb_faction: int,
            choice_win: curses.window,
            title_choice: str,
            index: int,
        ) -> Tuple[curses.window, int]:
        
        # Title window
        xt = int(round((curses.COLS-1)/2) - round(len(title)/2))
        yt = y_title - 3
        winTitle = curses.newwin(2, len(title), yt, xt)
        winTitle.addstr(0, 0, title)
        winTitle.refresh()
        
        choice_win.addstr(0, 0, title_choice+"\n")

        char_win.chgat(index, 0, curses.A_REVERSE)
        nb_choosen = 0
        
        self.display_options({
            self.data["directionalControls"]["north"] : "↑",
            self.data["directionalControls"]["south"] : "↓",
            self.data["enter_key"] : self.data["enter_value"],
            self.data["quit_key"] : self.data["quit_value"],
        }, index= 4)
        
        while nb_choosen < nb_faction:
            key = char_win.getkey()
            if key == self.data["directionalControls"]["north"]:
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == 0:
                    index = self.nb_classes - 1
                else:
                    index -= 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == self.data["directionalControls"]["south"]:
                char_win.chgat(index, 0, curses.A_NORMAL)
                if index == self.nb_classes - 1:
                    index = 0
                else:
                    index += 1
                char_win.chgat(index, 0, curses.A_REVERSE)
            elif key == "\n":
                char = globals()[self.all_classes[index].capitalize()]
                faction_list.append(char(faction))
                if (faction == Faction.ALLIANCE):
                    choice_win.addstr(nb_choosen+2, 0, self.all_classes[index])
                    choice_win.refresh()
                elif (faction == Faction.HORDE):
                    choice_win.addstr(nb_choosen+2, 0, self.all_classes[index])
                    choice_win.refresh()
                nb_choosen += 1
            elif key == self.data["quit_key"]:
                index = -1
                break
            char_win.refresh()
        self.options_window.clear()
        return winTitle, index
    
    def initialize_characters(self) -> None:
        self.character_list = self.alliance_list + self.horde_list
        self.character_list.sort(key=lambda x: x.priority, reverse=True)
        for index in range (len(self.alliance_list)):
            self.alliance_list[index].set_coords(x = 0, y = int((self.map.height - len(self.alliance_list)) / 2 + 2*index))
        for index in range (len(self.horde_list)):
            self.horde_list[index].set_coords(x = self.map.width - 1, y = int((self.map.height - len(self.horde_list)) / 2 + 2*index))

        
    def display_map(self,
                    text: str
                ) -> None :
        
        self.title_window.addstr(1, int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
        self.title_window.refresh()
        
        self.map_window.clear()
        self.map_window.addstr(0, 0, str(self.map))
        self.map_window.refresh()
        
    def play_turn(self,
                  character : Class,
                  round_number: int
                ) -> bool:
        
        while True:
            self.stdscr.clear()
            self.stdscr.refresh()
            
            text = f"{self.data['round']} {round_number}"
            text2 = f"{self.data['remainingMovements']} : {character.current_mobility}"
            
            self.title_window.clear()
            self.title_window.addstr(0, int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
            self.title_window.addstr(2, int(round((curses.COLS-1)/2) - round(len(text2)/2)), text2)
            self.title_window.refresh()
            
            self.map_window.clear()
            characterTurnText = self.data["characterTurn"] + character.content
            self.update_map()
            self.display_map(characterTurnText)
            self.map_window.chgat(character.y_coord*2 + 1,
                            character.x_coord*4 + 1,
                            3,
                            curses.A_REVERSE)
            self.map_window.refresh()
        
            self.display_options({
                self.data["directionalControls"]["north"] : "↑",
                self.data["directionalControls"]["south"] : "↓",
                self.data["directionalControls"]["east"] : "→",
                self.data["directionalControls"]["west"] : "←",
                self.data["skills"]["auto_attack_key"] : self.data["skills"]["auto_attack_value"],
                self.data["skills"]["skill_1_key"] : character.skill_1_name,
                self.data["skills"]["skill_2_key"] : character.skill_2_name,
                self.data["quit_key"] : self.data["quit_value"],
            })
            
            self.display_current_character_details(character)
            
            action = self.stdscr.getkey()

            if character.current_mobility > 0:
                if action == self.data["directionalControls"]["north"]:
                    direc = Direction.NORTH
                    if character.y_coord > 0 and self.square_is_empty_direction(character, direc):
                        self.map.reset_square_content(character.x_coord, character.y_coord)
                        character.move_with_direction(direc)
                elif action == self.data["directionalControls"]["west"]:
                    direc = Direction.WEST
                    if character.x_coord > 0 and self.square_is_empty_direction(character, direc):
                        self.map.reset_square_content(character.x_coord, character.y_coord)
                        character.move_with_direction(direc)
                elif action == self.data["directionalControls"]["south"]:
                    direc = Direction.SOUTH
                    if character.y_coord < self.map.height - 1 and self.square_is_empty_direction(character, direc):
                        self.map.reset_square_content(character.x_coord, character.y_coord)
                        character.move_with_direction(direc)
                elif action == self.data["directionalControls"]["east"]:
                    direc = Direction.EAST
                    if character.x_coord < self.map.width - 1 and self.square_is_empty_direction(character, direc):
                        self.map.reset_square_content(character.x_coord, character.y_coord)
                        character.move_with_direction(direc)
            if action == self.data["skills"]["skill_1_key"]:
                if not character.used_skill:
                    res = character.skill_1(self)
                    if res == False:
                        return res
            elif action == self.data["skills"]["skill_2_key"]:
                if not character.used_skill:
                    res = character.skill_2(self)
                    if res == False:
                        return res
            elif action == self.data["skills"]["auto_attack_key"]:
                if not character.used_auto_attack:
                    selected_square = self.select_ennemy_or_ally_target_square(character, character.current_range, False)
                    if selected_square == -1:
                        pass
                    elif selected_square is None:
                        return False
                    else:
                        target = self.get_character_from_square(selected_square)
                        character.auto_attack(target)
            elif action == self.data["pass_key"]:
                self.options_window.clear()
                break
            elif action == self.data["quit_key"]:
                return False
            self.update_map()
            self.map_window.refresh()
        return True


    def select_target_square(self,
                      character: Class,
                      skill_range: int,
                      x_start: int = 0,
                      y_start: int = 0,
                    )-> Square:
        self.map_window.clear()
        self.target_window.clear()
        self.update_map()
        self.display_map(self.data["targetSelection"])
        if x_start == 0 and y_start == 0 and character is not None:
            x_start, y_start = character.x_coord, character.y_coord
        selected_square = (x_start, y_start)
        
        self.display_options({
            self.data["directionalControls"]["north"] : "↑",
            self.data["directionalControls"]["south"] : "↓",
            self.data["directionalControls"]["east"] : "→",
            self.data["directionalControls"]["west"] : "←",
            self.data["enter_key"] : self.data["enter_value"],
            self.data["cancel_key"] : self.data["cancel_value"],
            self.data["quit_key"] : self.data["quit_value"],
        })
        
        while True:
            target = self.get_character_from_coords(selected_square[0], selected_square[1])
            if target is not None:
                self.display_target_character_details(target)
            else:
                self.target_window.clear()
                self.target_window.addstr(0, 0, f"{self.data['targetCharacter']} : {self.data['none']}")
                self.target_window.refresh()
            
            self.map_window.chgat(selected_square[1]*2 + 1,
                            selected_square[0]*4 + 1,
                            3,
                            curses.A_REVERSE)
            self.map_window.refresh()
            action = self.map_window.getkey()
            self.map_window.chgat(selected_square[1]*2 + 1,
                            selected_square[0]*4 + 1, 
                            3,
                            curses.A_NORMAL)
            self.map_window.refresh()
            x = selected_square[0]
            y = selected_square[1]
            if action == self.data["directionalControls"]["north"]:
                if y > 0:
                    y = y - 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == self.data["directionalControls"]["west"]:
                if x > 0:
                    x = x - 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == self.data["directionalControls"]["south"]:
                if y < self.map.height - 1:
                    y = y + 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == self.data["directionalControls"]["east"]:
                if x < self.map.width - 1:
                    x = x + 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == "\n":
                if not self.square_is_empty(x, y):
                    self.options_window.clear()
                    self.target_window.clear()
                    return self.map.square_list[selected_square]
            elif action == self.data["cancel_key"]:
                self.options_window.clear()
                self.target_window.clear()
                return -1
            elif action == self.data["quit_key"]:
                return None
    
    def target_area_range(self,
                          character: Class, 
                          range_area: Range,
                          skill_range: int,
                          x_start: int = 0,
                          y_start: int = 0
                        ) -> Square:
        self.map_window.clear()
        self.target_window.clear()
        self.update_map()
        self.display_map(self.data["areaSelection"])
        if x_start == 1 and y_start == 1 and character is not None:
            x_start, y_start = character.x_coord, character.y_coord
        selected_square = (x_start, y_start)
        
        self.display_options({
            self.data["directionalControls"]["north"] : "↑",
            self.data["directionalControls"]["south"] : "↓",
            self.data["directionalControls"]["east"] : "→",
            self.data["directionalControls"]["west"] : "←",
            self.data["enter_key"] : self.data["enter_value"],
            self.data["cancel_key"] : self.data["cancel_value"],
            self.data["quit_key"] : self.data["quit_value"],
        })
        
        if x_start == 0 and y_start == 0 and character is not None:
            x_start, y_start = character.x_coord, character.y_coord
        if x_start == 0:
            x_start += range_area.value
        if y_start == 0:
            y_start += range_area.value
        if x_start == self.map.width - 1:
            x_start -= range_area.value
        if y_start == self.map.height - 1:
            y_start -= range_area.value
        
        selected_square = (x_start, y_start)
        
        while True:
            self.target_window.clear()
                
            for j in range (selected_square[1] - range_area.value, selected_square[1] + range_area.value +1 , 1):
                for i in range (selected_square[0] - range_area.value, selected_square[0] + range_area.value + 1, 1):
                    self.map_window.chgat(j*2 + 1,
                                    i*4 + 1,
                                    3,
                                    curses.A_REVERSE)
            self.map_window.refresh()
            action = self.map_window.getkey()
                
            for j in range (selected_square[1] - range_area.value, selected_square[1] + range_area.value + 1, 1):
                for i in range (selected_square[0] - range_area.value, selected_square[0] + range_area.value + 1, 1):
                    self.map_window.chgat(j*2 + 1,
                                    i*4 + 1,
                                    3,
                                    curses.A_NORMAL)
            self.map_window.refresh()
            
            x = selected_square[0]
            y = selected_square[1]
            if action == self.data["directionalControls"]["north"]:
                if y > range_area.value:
                    y = y - 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == self.data["directionalControls"]["west"]:
                if x > range_area.value:
                    x = x - 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == self.data["directionalControls"]["south"]:
                if y < self.map.height - 1 - range_area.value:
                    y = y + 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == self.data["directionalControls"]["east"]:
                if x < self.map.width - 1 - range_area.value:
                    x = x + 1
                    if character.is_at_range_coords(x, y, skill_range):
                        selected_square = (x, y)
            elif action == "\n":
                selected_squares = []
                for j in range (selected_square[1] - range_area.value, selected_square[1] + range_area.value + 1, 1):
                    for i in range (selected_square[0] - range_area.value, selected_square[0] + range_area.value + 1, 1):
                        selected_squares.append((self.map.get_square_from_coords(i, j)))
                self.options_window.clear()
                self.target_window.clear()
                return selected_squares
            elif action == self.data["cancel_key"]:
                self.options_window.clear()
                self.target_window.clear()
                return -1
            elif action == self.data["quit_key"]:
                return None
            
    def validate_skill_launch(self) -> bool:
        self.update_map()
        self.display_map(self.data["skillValidation"])
        
        self.display_options({
            self.data["enter_key"] : self.data["enter_value"],
            self.data["cancel_key"] : self.data["cancel_value"],
        })
        while True:
            action = self.map_window.getkey()
            if action == self.data["cancel_key"]:
                return False
            elif action ==  "\n":
                return True
    
    def select_ennemy_or_ally_target_square(self,
                      character: Class,
                      skill_range: int,
                      ally: bool
                    )-> Square:
        x, y = 0, 0
        while True:
            selected_square = self.select_target_square(character, skill_range, x, y)
            if selected_square is None:
                return None
            elif selected_square == -1:
                return -1
            else:
                target = self.get_character_from_square(selected_square)
                if target is not None: 
                    if ally and target.faction == character.faction:
                        return selected_square
                    elif not ally and target.faction != character.faction:
                        return selected_square
                    else:
                        x, y = target.x_coord, target.y_coord

    def game_in_progress(self) -> bool:
        for elem in self.alliance_list:
            if elem.is_alive:
                return True
        for elem in self.horde_list:
            if elem.is_alive:
                return True    
        return False
    
    def who_is_at_range_ally(self, player: Class) -> list[str]:
        ret = []
        for elem in Game.character_list:
            if elem.faction == player.faction and player.is_at_range_character(elem):
                ret += elem.content
        return ret
    
    def who_is_at_range_enemy(self, player: Class) -> list[str]:
        ret = []
        for elem in Game.character_list:
            if elem.faction != player.faction and player.is_at_range_character(elem):
                ret += elem.content
        return ret
    
    def update_map(self) -> None:
        # self.map.reset_map_content()
        for elem in self.character_list:
            self.map.square_list[(elem.x_coord, elem.y_coord)].content = elem.content
            
    def square_is_empty_direction(self, current_char: Class, direction: Direction) -> bool:
        for char in self.character_list:
            if char != current_char:
                if current_char.y_coord + direction.value[1] == char.y_coord and current_char.x_coord + direction.value[0] == char.x_coord:
                    return False
        return True
            
    def square_is_empty(self, x: int, y: int) -> bool:
        for char in self.character_list:
            if char.x_coord == x and char.y_coord == y:
                return False
        return True

    def get_character_from_square(self, square: Square) -> Class:
        for elem in self.character_list:
            if elem.x_coord == square.x_coord and elem.y_coord == square.y_coord:
                return elem
        return None

    def get_character_from_coords(self, x: int, y: int) -> Class:
        for elem in self.character_list:
            if elem.x_coord == x and elem.y_coord == y:
                return elem
        return None
    
    def display_options(self, options: dict, index: int = 0) -> None:
        self.options_window.clear()
        for key, value in options.items():
            self.options_window.addstr(index, 0, f"{key} : {value}")
            index += 1
        self.options_window.refresh()
        
    def display_current_character_details(self, character: Class) -> None:
        self.character_window.clear()
        self.character_window.addstr(0, 0, f"{self.data['currentCharacter']} : {character.content} {character.current_hp} ({character.get_total_shield()})/{character.max_hp.value}")
        self.character_window.addstr(1, 0, f"{self.data['class']} : {character.__class__.__name__}")
        self.character_window.addstr(2, 0, f"{self.data['direction']} : {character.direction.name}")
        self.character_window.addstr(3, 0, f"{self.data['damage']} : {character.current_damage}")
        self.character_window.refresh()
    
    def display_target_character_details(self, character: Class, additional_text: str = "") -> None: 
        self.target_window.clear()
        self.target_window.addstr(0, 0, f"{self.data['targetCharacter']} : {character.content} {character.current_hp} / {character.max_hp.value}")
        self.target_window.addstr(1, 0, f"{self.data['class']} : {character.__class__.__name__}")
        self.target_window.addstr(2, 0, f"{self.data['direction']} : {character.direction.name}")
        self.target_window.addstr(3, 0, f"{self.data['damage']} : {character.current_damage}")
        self.target_window.addstr(4, 0, additional_text)
        self.target_window.refresh()
    
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
        text3 = data["goodbyeText3"]
        stdscr.addstr(int(round((curses.LINES-1)/2) - 1), int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
        stdscr.addstr(int(round((curses.LINES-1)/2)), int(round((curses.COLS-1)/2) - round(len(text2)/2)), text2)
        stdscr.addstr(int(round((curses.LINES-1)/2) + 1), int(round((curses.COLS-1)/2) - round(len(text3)/2)), text3)
        stdscr.refresh()
        stdscr.getch()
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
                self.square_list[(i, j)] = Square(i, j)
        pass

    def reset_square_content(self, x: int, y: int) -> None:
        self.square_list[(x, y)].reset_content()

    def reset_map_content(self) -> None:
        for i in range(self.width):
            for j in range(self.height):
                self.square_list[(i, j)].reset_content()
    
    def get_square_from_coords(self, x: int, y: int) -> Square:
        return self.square_list[(x, y)]
    
    def set_square_type_with_coords(self, x: int, y: int, square_type: SquareType, duration: int) -> None:
        square = self.get_square_from_coords(x, y)
        square.set_square_type(square_type, duration)

    def __str__(self) -> str:
        ret = ""
        for j in range(self.height + 1):
            for i in range(self.width):
                if i == 0:
                    if j == 0:
                        ret += "┌───"
                    elif j == self.height:
                        ret += "└───"
                    else: 
                        ret += "├───"
                if i == self.width - 1:
                    if j == 0:
                        ret += "┐"
                    elif j == self.height:
                        ret += "┘"
                    else: 
                        ret += "┤"
                else:
                    if j == 0:
                        ret += "┬───"
                    elif j == self.height:
                        ret += "┴───"
                    else:
                        ret += "┼───"
            if j != self.height:
                for i in range(self.width):
                    current_square = self.square_list[(i,j)]
                    ret += f"│{str(current_square)}"
                ret += "│"
        return ret
        