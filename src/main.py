#from game.Game import Game
#from characters.Class import Class
#from characters.classes import *
import curses
from curses import wrapper
from time import sleep

#game = Game()

# game.start_game()

def main(stdscr):
  stdscr.clear()
  
  game_pad = curses.newpad(curses.LINES-1, curses.COLS-1)
  test = stdscr.getch() #a=97, A=65
  game_pad.addstr(str(test))
  for i in range(10):
    stdscr.clear()
    stdscr.refresh()
    game_pad.refresh(0,0, 5,5+i, 10,10+i)
    sleep(0.5)
  # stdscr.getch()

wrapper(main)
"""
characters = Class.AVAILABLE_CLASSES
mob = []
chars = ""
print("CLASSES ORDERED BY max_hp")
for elem in characters:
    char = globals()[elem.capitalize()]
    max_hp = char.max_hp
    if max_hp not in mob:
        mob += [max_hp]
        chars +=(f"{max_hp.name} :")
        for character in characters:
            char = globals()[character.capitalize()]
            if char.max_hp == max_hp:
                chars += (f"- {character}")
        chars += "\n"
print (chars)
"""
