import pygame
from pygame.locals import *
from entities import User, Enemy
from object import Mur, Potion, Porte, Eau
from fonctions import *
from hud import *

import sys
import time
import zmq
import threading

from tkinter import *
from playsound import playsound


def choix1():
    global perso
    perso=1
    button1.configure(relief=SUNKEN)
    button2.configure(relief=RAISED)
    button3.configure(relief=RAISED)
    
def choix2():
    global perso
    perso=2
    button1.configure(relief=RAISED)
    button2.configure(relief=SUNKEN)
    button3.configure(relief=RAISED)

def choix3():
    global perso
    perso=3
    button1.configure(relief=RAISED)
    button2.configure(relief=RAISED)
    button3.configure(relief=SUNKEN)

perso=1
fen=Tk()
fen.geometry("250x300+200+0")
fen.configure(bg = "white")
user1=PhotoImage(file='images/user1.gif')
user2=PhotoImage(file='images/user2.gif')
user3=PhotoImage(file='images/user3.gif')
fen.title("LE JEU")
Label(fen,text="                ",bg="white").grid(row=1,column=0)
Label(fen,text="LE JEU \n\n ",bg="white").grid(row=0,column=2)
Button(fen,text="Jouer ",bg="white",command=fen.destroy).grid(row=1,column=2)
Label(fen,text="\n"*3,bg="white").grid(row=2,column=1)
button1=Button(fen, image=user1,bg="white",command=choix1, relief=SUNKEN)
button1.grid(row=3,column=1)
button2=Button(fen, image=user2,bg="white",command=choix2)
button2.grid(row=3,column=2)
button3=Button(fen, image=user3,bg="white",command=choix3)
button3.grid(row=3,column=3)
Label(fen,text="\n"*3,bg="white").grid(row=4,column=1)
Button(fen,text="Quitter",command=exit).grid(row=5,column=2)
jeu=0
playsound('musique_menu.mp3',block = False)

fen.mainloop()

### Initialisation du jeu
gameOver = False
pygame.init()
screen = pygame.display.set_mode((620,480))
pygame.display.set_caption('User 2')
screen.fill((50,60,50))
pygame.display.update()


### Création des utilisateurs
user = User(screen,2, perso)
coop = User(screen,1,1)
hud = HUD(screen)

### Création de la connection réseau
context = zmq.Context()
usersChan = context.socket(zmq.PAIR)
usersChan.connect("tcp://127.0.0.1:1111".format(user.id))


### Génération de la MAP

data = usersChan.recv_pyobj()
murs, potions= [], []
portes = []
eaus = []
enemies = []


for mur in data["murs"]:
    murs.append(Mur(screen,*mur["pos"],mur["genre"]))

for potion in data["potions"]:
    potions.append(Potion(screen,*potion["pos"],potion["type"]))

for porte in data["portes"]:
    portes.append(Porte(screen,*porte["pos"]))

for eau in data["eaus"]:
    eaus.append(Eau(screen,*eau["pos"]))

for enemy in data["enemies"]:
    enemies.append(Enemy(screen,*enemy["pos"],enemy["level"],enemy["type"]))


# Thread parralléle qui récuperre les données
def recv(usersChan):
    global coop, gameOver,murs,potions,portes,eaus,enemies
    while True:
        if gameOver == True:
            print("gameOver")
            exit()
            return



        try:
            data = usersChan.recv_pyobj(flags=zmq.NOBLOCK)

            if data["changement"]:
                user.pos = data["coop"]["pos"]
                murs, potions= [], []
                portes = []
                eaus = []
                enemies = []


                for mur in data["murs"]:
                    murs.append(Mur(screen,*mur["pos"],mur["genre"]))

                for potion in data["potions"]:
                    potions.append(Potion(screen,*potion["pos"],potion["type"]))

                for porte in data["portes"]:
                    portes.append(Porte(screen,*porte["pos"]))

                for eau in data["eaus"]:
                    eaus.append(Eau(screen,*eau["pos"]))

                for enemy in data["enemies"]:
                    enemies.append(Enemy(screen,*enemy["pos"],enemy["level"],enemy["type"]))

            coop.pos = data["user"]["pos"]
            coop.vie = data["user"]["vie"]
            coop.attaque = data["user"]["attaque"]
            coop.defense = data["user"]["defense"]
            coop.level = data["user"]["level"]
            coop.xp= data["user"]["xp"]
            ### Supprimer objets qui ne sont pas en communs entre 2 listes python
            for potion in potions:
                ok = False
                for p in data["potions"]:
                    if potion.pos == p["pos"]:
                        ok = True
                if ok == False:
                    potions.remove(potion)

            for enemy in enemies:
                ok = False
                for e in data["enemies"]:
                    if enemy.pos == e["pos"]:
                        enemy.vie = e["vie"]
                        ok = True
                if ok == False:
                    enemies.remove(enemy)


            refresh()
        except zmq.ZMQError as err:
            pass

def refresh():

    screen.fill((50,60,50))
    hud.show(user,coop)
    user.show()
    coop.show()
    for enemy in enemies:
        enemy.show()
    for mur in murs:
        mur.show()
    for potion in potions:
        potion.show()
    for porte in portes:
        porte.show()
    for eau in eaus:
        eau.show()
    user.show()
    coop.show()
    pygame.display.flip()
    pygame.display.update()

threadRecv = threading.Thread(target=recv, args=(usersChan,))
threadRecv.start()

while not gameOver:
    if user.vie <= 0:
        gameOver = True

    if coop.vie <= 0:
        gameOver = True

    for event in pygame.event.get():

        # Alt + F4 ou fléche en haut
        if event.type == QUIT:
            gameOver = True
            print("game over")

            # Si touche pressée
        if event.type == KEYDOWN:
            action = 1
            if event.key == K_UP:
                coord = (0,-1)
            elif event.key == K_DOWN:
                coord = (0,1)
            elif event.key == K_LEFT:
                coord = (-1,0)
            elif event.key == K_RIGHT:
                coord = (1,0)
            else:
                action = 0

            if action != 0:
                user.mouvement(coord)
                if user.pos == coop.pos:
                    user.mouvement((-coord[0],-coord[1]))

            for enemy in enemies:
                if enemy.pos == user.pos:
                    # Attaquer :
                    enemy.vie -= user.attaque + user.arme
                    user.vie -= enemy.defense

                    if user.vie <= 0:
                        user.vie = 0
                        gameOver == True

                    # print("Vie restante :", user.vie, "Vie enemmi :", enemy.vie)
                    if enemy.vie <= 0:
                        user.xp += enemy.level
                        enemies.remove(enemy)
                    # Revenir en arriére
                    else:
                        user.mouvement((-coord[0],-coord[1]))

            if user.xp >= user.level * 2:
                user.levelUP()


            for mur in murs:
                if mur.pos == user.pos :
                    if mur.genre == "lave":
                        user.vie -= 15
                    elif mur.genre == "pont":
                        pass
                    elif mur.genre == "levier":
                        pass
                    else:
                        user.mouvement((-coord[0],-coord[1]))

            for eau in eaus:
                if eau.pos == user.pos :
                    user.mouvement((-coord[0],-coord[1]))

            for potion in potions:
                if user.pos == potion.pos:
                    if potion.type == "heal":
                        user.heal()
                    elif potion.type == "atk":
                        user.atk()
                    elif potion.type == "atkboss":
                        for i in range (20):
                            user.atk()
                    elif potion.type == "xp":
                        user.levelUP()
                    potions.remove(potion)

            try:
                message = setData(user,coop,murs,potions,portes,eaus,enemies,False)
                usersChan.send_pyobj(message)

            except zmq.ZMQError as err:
                print ("Error while trying to send the value " + message + " : " + str(err))


            refresh()






        pygame.display.flip()
    pygame.display.update()
    pygame.time.wait(10)
