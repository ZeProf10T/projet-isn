import pygame
# Importe les constantes, ex : K_UP
from pygame.locals import *

class HUD(object):

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Calibri", 24)


    def show(self,user,coop):
        if user.vie <= 15:
            color = (255,0,0)
        else:
            color = (255,255,255)

        if coop.vie <= 15:
            ccolor = (255,0,0)
        else:
            ccolor = (255,255,255)

        self.vie = self.font.render("Vie : " + str(user.vie), True, color)
        self.attaque = self.font.render("Attaque : " + str(user.attaque), True, (255,255,255))
        self.level = self.font.render("Level : " + str(user.level), True, (255,255,255))
        self.xp = self.font.render("XP : " + str(user.xp), True, (255,255,255))

        self.cvie = self.font.render("Vie : " + str(coop.vie), True, ccolor)
        self.cattaque = self.font.render("Attaque : " + str(coop.attaque), True, (255,255,255))
        self.clevel = self.font.render("Level : " + str(coop.level), True, (255,255,255))
        self.cxp = self.font.render("XP : " + str(coop.xp), True, (255,255,255))

        self.screen.blit(self.vie,(500,20))
        self.screen.blit(self.attaque, (500,50))
        self.screen.blit(self.level,(500,80))
        self.screen.blit(self.xp,(500,110))

        self.screen.blit(self.cvie,(500,240))
        self.screen.blit(self.cattaque, (500,270))
        self.screen.blit(self.clevel,(500,300))
        self.screen.blit(self.cxp,(500,330))
