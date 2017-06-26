# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame
import sys
from pygame.locals import *

class ImageProjector:
    
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
    
    def projectImage(self,image,x,y,r):   
    
        #fill background with in black
        self.screen.fill((0,0,0))
    
        image2 = pygame.transform.scale(image.copy(),(2*r,2*r))
    
        #place image at new location
        self.screen.blit(image2,(int(x),int(y)))
    
        #Updates the display
        pygame.display.flip()
    
    def check_keys(self):
        events = pygame.event.get()
        for event in events:
            if event.type == KEYUP:
                if event.key == pygame.K_q:
                    return True
                elif event.key == pygame.K_x:
                    return True
            elif event.type == QUIT:
                return True
            else:
                return False
            
    def stopProjecting(self):
        
        pygame.display.quit()
        pygame.quit()
