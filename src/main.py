from characters.Class import Class
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from game.Game import Game


# Définition des classes de personnages pour les menus déroulants
characters = Class.AVAILABLE_CLASSES
SQUARE_SIZE: int = 50
MAP_WIDTH: int = 640
MAP_HEIGHT: int = 480

images = {}
for elem in characters:
    images[elem] = f"ressources/img/characters/{elem}.jpeg"


char_window = tk.Tk()

padding_width:int = (char_window.winfo_screenwidth()-MAP_WIDTH)//2
padding_height:int = (char_window.winfo_screenheight()-MAP_HEIGHT)//2

char_window.title("Character selection")
char_window.iconbitmap("ressources/img/addons/logo.ico")
char_window.config(bg = "#b6b5b5")
char_window.geometry(f"{MAP_WIDTH}x{MAP_HEIGHT}+{padding_width}+{padding_height}")
char_window.resizable(width=0, height=0)

launch_button = tk.Button(char_window, text = "Launch game")
launch_button.pack()

char_window.mainloop()
