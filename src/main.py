from characters.Class import Class
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk




# char1 = Class("Berserker")
# char2 = Class("Archer")

# Définition des classes de personnages pour les menus déroulants
# characters = Class.available_classes

characters = ['Warrior', 'Mage', 'Rogue', 'Archer']
images = {
    'Warrior': 'ressources/img/characters/warrior.jpg',
    'Mage': 'ressources/img/characters/warrior.jpg',
    'Rogue': 'ressources/img/characters/warrior.jpg',
    'Archer': 'ressources/img/characters/warrior.jpg'
}


class CharacterSelectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélection de Personnage")

        # Créer les widgets
        self.create_widgets()

    def create_widgets(self):
        # Menu déroulant pour l'équipe 1
        self.team1_label = tk.Label(self.root, text="Équipe 1")
        self.team1_label.grid(row=0, column=0, padx=10, pady=10)
        self.team1_var = tk.StringVar()
        self.team1_menu = ttk.Combobox(self.root, textvariable=self.team1_var, values=characters)
        self.team1_menu.grid(row=1, column=0, padx=10, pady=10)
        
        # Menu déroulant pour l'équipe 2
        self.team2_label = tk.Label(self.root, text="Équipe 2")
        self.team2_label.grid(row=0, column=1, padx=10, pady=10)
        self.team2_var = tk.StringVar()
        self.team2_menu = ttk.Combobox(self.root, textvariable=self.team2_var, values=characters)
        self.team2_menu.grid(row=1, column=1, padx=10, pady=10)
        
        # Bouton pour lancer la partie
        self.start_button = tk.Button(self.root, text="Lancer la Partie", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Zone pour afficher la grille
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg='white')
        self.canvas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Charger les images
        self.images = {}
        for character, path in images.items():
            img = Image.open(path)
            img = img.resize((40, 40), Image.Resampling.LANCZOS)  # Mise à jour du mode de redimensionnement
            self.images[character] = ImageTk.PhotoImage(img)

    def start_game(self):
        self.canvas.delete("all")
        team1_char = self.team1_var.get() if self.team1_var.get() else ''
        team2_char = self.team2_var.get() if self.team2_var.get() else ''

        # Dessiner la grille
        for i in range(20):  # 20 colonnes
            for j in range(10):  # 10 lignes
                x1, y1 = i * 40, j * 40
                x2, y2 = x1 + 40, y1 + 40
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black')
        
        # Afficher les personnages
        if team1_char and team1_char in self.images:
            self.canvas.create_image(0, 200, anchor='nw', image=self.images[team1_char])
        if team2_char and team2_char in self.images:
            self.canvas.create_image(800, 200, anchor='ne', image=self.images[team2_char])

# Création de la fenêtre principale
root = tk.Tk()
app = CharacterSelectionApp(root)
root.mainloop()
