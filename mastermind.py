import tkinter as tk
from random import *

LARGEUR = 1000
HAUTEUR = 600
couleur = ["red","blue","cyan","yellow","teal","indigo","pink","gold"]

def mastermind():
    pass

def clic(event):
    X=event.x
    Y=event.y
    if 500 < Y < 570:

        if 50 < X < 120:
            print(couleur[0])
        elif 170 < X < 240:
            print(couleur[1])
        elif 290 < X < 360:
            print(couleur[2])
        elif 410 < X < 480:
            print (couleur[3])
        elif 530 < X < 600:
            print (couleur[4])
        elif 650 < X < 720:
            print (couleur[5])
        elif 770 < X < 840:
            print (couleur[6])
        elif 890 < X < 960:
            print (couleur[7])

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

xmin=LARGEUR//3
ymin=HAUTEUR//6
print(xmin,ymin)
xmax=xmin+25
ymax=ymin+25
for j in range (10):
    for i in range(4):
        compteur=i*5
        cercle = canvas.create_oval(xmin +30*i+compteur, ymin +30*j, xmax +30*i+compteur, ymax +30*j, fill="white")

for i in range (8):
    compteur=i*70
    cercle = canvas.create_oval(50+50*i+compteur, 500, 120+50*i+compteur, 570, fill=couleur[i])

canvas.bind('<Button-1>',clic)
racine.mainloop() 
# Fin de fenetre 
