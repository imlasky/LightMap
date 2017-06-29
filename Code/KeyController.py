# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame
from pygame.locals import *

#class to control projection.
#Escape, x, q  quit display
#Space         pause/start display

class KeyController:
    
    def __init__(self,screen):
        self.screen = screen
     
    def check_keys(self):
        self.events = pygame.event.get()
        self.exit_flag = False
        self.enter_flag = False
        for event in self.events:
            if event.type == KEYUP:
                if event.key == pygame.K_q:
                    self.exit_flag = True
                elif event.key == pygame.K_x:
                    self.exit_flag = True
                elif event.key == pygame.K_ESCAPE:
                    self.exit_flag = True
                elif event.key == pygame.K_RETURN:
                    self.enter_flag = True
            elif event.type == QUIT:
                self.exit_flag = True

        return (self.exit_flag, self.enter_flag)
            
            