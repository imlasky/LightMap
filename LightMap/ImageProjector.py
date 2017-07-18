# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame
import sys
from pygame.locals import *
import KeyController as kc

class ImageProjector:
    
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.myKc = kc.KeyController(self.screen)
    
    def projectImage(self,image,x,y,r):   
    
        #fill background with in black
        self.screen.fill((0,0,0))
        
        pygame.mouse.set_visible(False)
        
        image = pygame.transform.rotate(image.copy(),-90)
        image = pygame.transform.flip(image.copy(),True,False)
    
        image2 = pygame.transform.scale(image.copy(),(2*r,2*r))
            
        im_rect = image2.get_rect()
    
        #place image at new location
        if im_rect.width and im_rect.height:
            print(x-im_rect.width/2)
            self.screen.blit(image2,(int(x-im_rect.width/2),int(y - im_rect.height/2)))
    
        #Updates the display
        pygame.display.flip()
    
    def event(self):
        
        flags = self.myKc.check_keys()
        return flags
#        self.events = pygame.event.get()
#        for event in events:
#            if event.type == KEYUP:
#                if event.key == pygame.K_q:
#                    return True
#                elif event.key == pygame.K_x:
#                    return True
#                elif event.key == pygame.K_ESCAPE:
#                    return True
#            elif event.type == QUIT:
#                return True
#            else:
#                return False
            
    def stopProjecting(self):
        
        pygame.display.quit()
        pygame.quit()
