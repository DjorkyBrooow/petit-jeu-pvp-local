import time
import traceback
from game.Game import Game
from characters.Class import Class
from characters.classes import *
import curses


def display_main_menu(data):
    
    title = data["titleText"]

    #calculate where to place the title
    titleWidth = len(max(title, key=len))
    titleHeight = len(title)+1
    x = int(round((curses.COLS-1)/2) - round(titleWidth/2))
    y = int(round((curses.LINES-1)/2) - round(titleHeight/2))
    #create window for title
    titleWindow = curses.newwin(titleHeight, titleWidth, y, x)
    # #add text to window
    for i in range(0, len(title)):
        titleWindow.addstr(i, 0, title[i])

    mainMenuText = data["mainMenuText"]
    x1 = int(round((curses.COLS-1)/2) - round(len(mainMenuText)/2))
    y1 = y + titleHeight+ 1
    mainMenuWindow1 = curses.newwin(1, len(mainMenuText)+1, y1, x1)
    mainMenuWindow1.addstr(0, 0, mainMenuText)

    mainMenuText2 = data["mainMenuText2"]
    x2 = int(round((curses.COLS-1)/2) - round(len(mainMenuText2)/2))
    y2 = y1 + 1
    mainMenuWindow2 = curses.newwin(1, len(mainMenuText2) + 1, y2, x2)
    mainMenuWindow2.addstr(0, 0, mainMenuText2)

    titleWindow.refresh()
    mainMenuWindow1.refresh()
    mainMenuWindow2.refresh()

    key = titleWindow.getkey()

    titleWindow.clear()
    mainMenuWindow1.clear()
    mainMenuWindow2.clear()

    return key

def launch_game(stdscr):
    stdscr.clear()
    data = Game.load_data()
    key = display_main_menu(data)

    if key == 'x':
        stdscr.clear()
        text = data["goodbyeText"]
        text2 = data["goodbyeText2"]
        stdscr.addstr(int(round((curses.LINES-1)/2)), int(round((curses.COLS-1)/2) - round(len(text)/2)), text)
        stdscr.addstr(int(round((curses.LINES-1)/2) + 1), int(round((curses.COLS-1)/2) - round(len(text2)/2)), text2)
        stdscr.refresh()
        time.sleep(3)
    if key == 'c':
        pass
    else:
        game = Game(stdscr)
        game.data = data
        game.start_game()
        return
    


def main(stdscr):

    # key = stdscr.getkey()
    # while key != 'q':
    #     stdscr.clear()
    #     stdscr.addstr(0, 0, key)
    #     stdscr.refresh()
    #     key = stdscr.getkey()
    
    # COLORS
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    try:
        launch_game(stdscr)
        #when game ends quit curses
        curses.endwin()
    #quit curses and print exception if there was an error
    except Exception:
        curses.endwin()
        traceback.print_exc()
  
if __name__ == '__main__':
    curses.wrapper(main)
