import tkinter as tk
from random import *

#Variable globale 

LARGEUR = 1000
HAUTEUR = 600

xmin=LARGEUR//3
ymin=HAUTEUR//6
xmax=xmin+25
ymax=ymin+25

cpt = 0
cpt_list = 0
couleur = ["red","blue","cyan","yellow","teal","indigo","pink","gold"]
code = []
code_t = []
reponse = [str(couleur[randint(0, 7)]) for i in range(4)]
print(reponse)
#Fonctions

def mastermind():
    pass

def debut():
    global cpt
    cpt += 1
    if cpt % 2 == 0 :
        rect_nr = canvas.create_rectangle(10,30,100,65, fill="black")
        mode_text = canvas.create_text(50,50,text = "1 joueur", fill="white", font=('Times', '14'))
        reponse = [str(couleur[randint(0, 7)]) for i in range(4)]
        print(reponse)
        return reponse
    else:
        rect_nr = canvas.create_rectangle(10,30,100,65, fill="black")
        mode_text = canvas.create_text(50,50,text = "2 joueurs", fill="white", font=('Times', '14'))


def start():
    for j in range (10):
        for i in range(4):
            compteur=i*5
            cercle = canvas.create_oval(xmin +30*i+compteur, ymin +30*j, xmax +30*i+compteur, ymax +30*j, fill="white", tags = "inconnu")
    for i in range (8):
        compteur=i*70
        cercle = canvas.create_oval(50+50*i+compteur, 500, 120+50*i+compteur, 570, fill=couleur[i], tags = [couleur[i], "choix"])

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
    if len(code_t) < 10:
        if len(code) < 4:
            code.append(color)
            prise_couleur(code)
        if len(code) == 4:
            verifie(code)
            code_t.append(list(code))
            code.clear() 
            
    else:
        perdu = canvas.create_text(500,450,text = "perdu", fill="white", font=('Times', '26'))

def prise_couleur(liste):
    for i in range(len(liste)):
        cercle = canvas.create_oval(xmin +35*i, ymin + 30*(len(code_t)), xmax +35*i, ymax + 30*(len(code_t)), fill=liste[i])

#pour verifier la reponse
def verifie(liste_code):
    #copie de la liste pour pas modifier
    rep = list(reponse)
    liste = list(liste_code)
    list_rep = []
    #Bien placé
    for i in range(4):
        if rep[i] == liste[i]:
            list_rep.append("green")
            rep[i] = "white"
            liste[i] = "*"
    #Mal placé
    for i in range(4):
        if rep[i] == liste[0] or rep[i] == liste[1] or rep[i] == liste[2] or rep[i] == liste[3]:
            list_rep.append("red")
            liste[liste.index(rep[i])] = "*"
            rep[i] = "white"
    list_rep.sort()
    for i in range(len(list_rep)):
        cercle = canvas.create_oval(500+12*i, 110 + 30*len(code_t), (500+10)+12*i, 120+ 30*len(code_t), fill=list_rep[i])
    if list_rep == ["green","green","green","green"]:
        gagné = canvas.create_text(500,450,text = "Gagné", fill="white", font=('Times', '26'))
    list_rep.clear()




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
bouton_change= tk.Button(racine, text="changer de mode", command=lambda: debut())
bouton_change.grid(row=1, column=4)
titre = canvas.create_text(500,50,text = "MASTERMIND", fill="white", font=('Times', '24'))
mode_text = canvas.create_text(50,50,text = "1 joueur", fill="white", font=('Times', '14'))



start()
canvas.bind('<Button-1>',clic)

racine.mainloop() 
# Fin de fenetre 