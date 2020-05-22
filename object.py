import pygame
from pygame.locals import *

class Mur(object):

    def __init__(self,screen,x,y, genre):
        self.pos = [x,y]
        self.genre = genre
        self.screen = screen
        if self.genre == "mur":
            self.image = pygame.image.load("images/mur.png").convert()
        elif self.genre == "lave":
            self.image = pygame.image.load("images/lave.png").convert()
        elif self.genre == "eau":
            self.image = pygame.image.load("images/eau.png").convert()
        elif self.genre == "pierre":
            self.image=pygame.image.load("images/pierre.png").convert()
        elif self.genre == "pont":
            self.image = pygame.image.load("images/pont.png").convert()
        elif self.genre == "levier":
            self.image= pygame.image.load("images/levier.png").convert()
        else:
            self.image = pygame.image.load("images/mur.png").convert()
        self.screen.blit(self.image, self.pos)

    def show(self):
        self.screen.blit(self.image, self.pos)

class Potion(object):

    def __init__(self, screen, x,y, type):
        self.type = type
        self.pos = [x,y]
        self.screen = screen
        if self.type == "heal":
            self.image = pygame.image.load("images/heal.png")
        elif self.type == "atk":
            self.image = pygame.image.load("images/atk.png")
        elif self.type == "xp":
            self.image = pygame.image.load("images/def.png")
        elif self.type == "atkboss":
            self.image = pygame.image.load("images/atkboss.png")
        self.screen.blit(self.image, self.pos)

    def show(self):
        self.screen.blit(self.image, self.pos)

class Porte(object):

    def __init__(self, screen,x,y):
        self.pos = [x,y]
        self.screen = screen
        self.image = pygame.image.load("images/porte.png").convert()

        self.screen.blit(self.image, self.pos)

    def show(self):
        self.screen.blit(self.image, self.pos)

class Eau(object):

    def __init__(self, screen,x,y):
        self.pos = [x,y]
        self.screen = screen
        self.image = pygame.image.load("images/mur2.2.png").convert()

        self.screen.blit(self.image, self.pos)

    def show(self):
        self.screen.blit(self.image, self.pos)
