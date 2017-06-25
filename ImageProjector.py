# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame
import sys

class ImageProjector:
    
    def __init__(self):
        
        self.screen = pygame.display.set_mode((640,480))
        pygame.init()
    
    def projectImage(self,image,x,y,r):   
    
        #fill background with in black
        self.screen.fill((0,0,0))
    
        image2 = pygame.transform.scale(image.copy(),(2*r,2*r))
    
        #place image at new location
        self.screen.blit(image2,(int(x),int(y)))
    
        #Updates the display
        pygame.display.flip()
    