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
        self.up_flag = False
        self.down_flag = False
        self.right_flag = False
        self.left_flag = False
        for event in self.events:
            if event.type == KEYUP:
                if event.key == pygame.K_q:
                    self.exit_flag = True
                elif event.key == pygame.K_x:
                    self.exit_flag = True
                elif event.key == pygame.K_ESCAPE:
                    self.exit_flag = True
                elif event.key == pygame.K_UP:
                    self.up_flag = True
                elif event.key == pygame.K_DOWN:
                    self.down_flag = True
                elif event.key == pygame.K_RIGHT:
                    self.right_flag = True
                elif event.key == pygame.K_LEFT:
                    self.left_flag = True
            elif event.type == QUIT:
                self.exit_flag = True

        return (self.exit_flag, self.up_flag, self.down_flag, self.right_flag, self.left_flag)
            
            