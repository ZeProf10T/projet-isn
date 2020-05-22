import pygame
from pygame.locals import *
import random

class Enemy():

    def __init__(self,screen,x,y,level, type):
        self.screen = screen
        self.type = type


        self.image = pygame.image.load("images/enemy{}.png".format(self.type)).convert()
        self.taille = [self.image.get_width(),self.image.get_height()]
        self.pos = [x,y]


        if type==3 or type==2:
            self.vie=4*level
        elif type == 4:
            self.vie=1
        elif type==9:
            self.vie = 85
        else:
            self.vie =  6 * level
        if type==4 or type==9:
            self.defense=0
        elif type==3:
            self.defense=3*level
        else:
            self.defense = 2 * level
        self.level = level
        self.screen.blit(self.image, self.pos)

    def show(self):
        self.screen.blit(self.image, self.pos)

class User(object):

    def __init__(self,screen,id, design):

        self.screen = screen
        self.image = pygame.image.load("images/user{}.png".format(design)).convert()
        self.taille = [self.image.get_width(),self.image.get_height()]
        self.id = id
        if id == 1:
            self.pos = [32,160]
        elif id == 2:
            self.pos = [32,192]

        self.vie = 50
        self.attaque = 3
        self.defense = 3
        self.level = 1
        self.arme = 0
        self.xp = 0
        self.screen.blit(self.image, self.pos)

    def levelUP(self):
        self.level += 1
        self.attaque += 2
        self.xp = 0

    def show(self):
        self.screen.blit(self.image, self.pos)

    def mouvement(self,coord):
        self.pos[0] += coord[0] * 32
        self.pos[1] += coord[1] * 32

    def heal(self):
        self.vie = 50

    def atk(self):
        self.attaque += 2
