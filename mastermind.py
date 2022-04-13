import tkinter as tk
from random import *

LARGEUR = 1500
HAUTEUR = 1300

def mastermind():
    pass




# Fenetre Pricipalee
racine = tk.Tk() 
racine.title("Mastermind")
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid(columnspan=5, row = 0, column = 0)
bouton_aide= tk.Button(racine, text="aide", command=lambda: mastermind())
bouton_aide.grid(row=1, column=0)
bouton_retrouve= tk.Button(racine, text="retrouver la sauvegarde", command=lambda: mastermind())
bouton_retrouve.grid(row=1, column=1)
bouton_sauvegarde= tk.Button(racine, text="sauvegarder", command=lambda: mastermind())
bouton_sauvegarde.grid(row=1, column=2)
bouton_retour= tk.Button(racine, text="retour", command=lambda: mastermind())
bouton_retour.grid(row=1, column=3)
bouton_change= tk.Button(racine, text="changer de mode", command=lambda: mastermind())
bouton_change.grid(row=1, column=4)

xmin=500
ymin=300
xmax=550
ymax=350
for j in range (10):
    for i in range(4):
        cercle = canvas.create_oval(xmin +75*i, ymin +75*j, xmax +75*i, ymax +75*j, fill="white")

for i in range (8):
    cercle = canvas.create_oval(150 +i*200, 1100,220 + i*200, 1170,  fill="white")
racine.mainloop() 
# Fin de fenetre 
