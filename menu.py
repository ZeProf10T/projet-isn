from tkinter import *
from playsound import playsound
import time


def jouer():
    jeu=1

def choix1():
    perso=1

def choix2():
    perso=2

def choix3():
    perso=3


fen=Tk()
fen.geometry("250x300+200+0")
fen.configure(bg = "white")
user1=PhotoImage(file='images/user1.gif')
user2=PhotoImage(file='images/user2.gif')
user3=PhotoImage(file='images/user3.gif')
fen.title("LE JEU")
Label(fen,text="                ",bg="white").grid(row=1,column=0)
Label(fen,text="LE JEU \n\n ",bg="white").grid(row=0,column=2)
Button(fen,text="Jouer ",bg="white",command=jouer).grid(row=1,column=2)
Label(fen,text="\n"*3,bg="white").grid(row=2,column=1)
Button(fen, image=user1,bg="white",command=choix1).grid(row=3,column=1)
Button(fen, image=user2,bg="white",command=choix2).grid(row=3,column=2)
Button(fen, image=user3,bg="white",command=choix3).grid(row=3,column=3)
Label(fen,text="\n"*3,bg="white").grid(row=4,column=1)
Button(fen,text="Quitter",command=fen.destroy).grid(row=5,column=2)
jeu=0
playsound('musique_menu.mp3',block = False)

fen.mainloop
