# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame
import sys

class imageProjector:
    
    def __init__(self,screen):
        self.screen = screen
    
    def projectImage(self,image,(x,y)):   
    
        #fill background with in black
        self.screen.fill((0,0,0))
    
        #place image at new location
        self.screen.blit(image,(int(x),int(y)))
    
        #Updates the display
        pygame.display.flip()
    
        return