import tkinter as tk
from random import *

#Variable globale 

LARGEUR = 1000
HAUTEUR = 600

xmin=LARGEUR//3
ymin=HAUTEUR//6
xmax=xmin+25
ymax=ymin+25

couleur = ["red","blue","cyan","yellow","teal","indigo","pink","gold"]
code = []
reponse = ["red","blue","cyan","yellow"]
#Fonctions

def mastermind():
    pass

def clic(event):
    X=event.x
    Y=event.y
    if 500 < Y < 570:
        if 50 < X < 120:
            lecture_clic(couleur[0],code)
        elif 170 < X < 240:
            lecture_clic(couleur[1],code)
        elif 290 < X < 360:
            lecture_clic(couleur[2],code)
        elif 410 < X < 480:
            lecture_clic(couleur[3],code)
        elif 530 < X < 600:
            lecture_clic(couleur[4],code)
        elif 650 < X < 720:
            lecture_clic(couleur[5],code)
        elif 770 < X < 840:
            lecture_clic(couleur[6],code)
        elif 890 < X < 960:
            lecture_clic(couleur[7],code)

def lecture_clic(color,code):
    if len(code) < 4:
        code.append(color)
        prise_couleur(code)
    if len(code) == 4:
        verifie(code)

def prise_couleur(liste):
    for i in range(len(liste)):
        compteur=i*5
        cercle = canvas.create_oval(xmin +30*i+compteur, ymin, xmax +30*i+compteur, ymax, fill=liste[i])

def verifie(liste):
    list_rep = []
    for i in range(4):
        if reponse[i] == liste[i]:
            list_rep.append("green")
        elif liste[i] == reponse[0] or liste[i] == reponse[1] or liste[i] == reponse[2] or liste[i] == reponse[3]:
            list_rep.append("red")
    list_rep.sort()
    for i in range(len(list_rep)):
        cercle = canvas.create_oval(500+12*i, 110, (500+10)+12*i, 120, fill=list_rep[i])


def retour():
    code[-1] = "white"
    prise_couleur(code)



# Fenetre Pricipalee
racine = tk.Tk() 
racine.title("Mastermind")
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid(columnspan=5, row = 0, column = 0)

#Boutons
bouton_aide= tk.Button(racine, text="aide", command=lambda: mastermind())
bouton_aide.grid(row=1, column=0)
bouton_retrouve= tk.Button(racine, text="retrouver la sauvegarde", command=lambda: mastermind())
bouton_retrouve.grid(row=1, column=1)
bouton_sauvegarde= tk.Button(racine, text="sauvegarder", command=lambda: mastermind())
bouton_sauvegarde.grid(row=1, column=2)
bouton_retour= tk.Button(racine, text="retour", command=lambda: retour())
bouton_retour.grid(row=1, column=3)
bouton_change= tk.Button(racine, text="changer de mode", command=lambda: mastermind())
bouton_change.grid(row=1, column=4)
texte = canvas.create_text(500,50,text = "MASTERMIND", fill="white", font=('Times', '24'))

print(xmin,ymin)
#Grille de jeu

for j in range (10):
    for i in range(4):
        compteur=i*5
        cercle = canvas.create_oval(xmin +30*i+compteur, ymin +30*j, xmax +30*i+compteur, ymax +30*j, fill="white", tags = "inconnu")

for i in range (8):
    compteur=i*70
    cercle = canvas.create_oval(50+50*i+compteur, 500, 120+50*i+compteur, 570, fill=couleur[i], tags = [couleur[i], "choix"])

#couleur_choisie = []
#def interpretation_clic (event) :
#    cercle_choisi = canvas.find_closest(event.x, event.y)
#    tag_choisi = canvas.gettags(cercle_choisi)
#    global couleur_choisie
#    if "choix" in tag_choisi :
#        couleur_choisie.append(tag_choisi[0])
#    elif "inconnu" in tag_choisi :
#        canvas.itemconfig(cercle_choisi, fill = couleur_choisie[-1])
#        couleur_choisie = []

canvas.bind('<Button-1>',clic)
#canvas.bind('<Button-3>', interpretation_clic)
racine.mainloop() 
# Fin de fenetre 