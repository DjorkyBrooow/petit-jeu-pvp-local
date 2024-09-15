from game.Game import Game
from characters.Class import Class
from characters.classes import *


characters = Class.AVAILABLE_CLASSES


game = Game()

# game.start_game()

mob = []
print("CLASSES ORDERED BY MOBILITY")
for elem in characters:
    char = globals()[elem.capitalize()]
    mobility = char.mobility
    if mobility not in mob:
        mob += [mobility]
        print(f"{mobility.name} :")
        for character in characters:
            char = globals()[character.capitalize()]
            if char.mobility == mobility:
                print(f"- {character}")


