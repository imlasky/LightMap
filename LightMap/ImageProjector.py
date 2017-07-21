# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame
from pygame.locals import *
import KeyController as kc

class ImageProjector:
    
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((1280,960))
        self.key_controller = kc.KeyController(self.screen)
    
    def project_image(self,image,x,y,r):   
    
        #fill background with in black
        self.screen.fill((0,0,0))
        
        pygame.mouse.set_visible(False)
        
        image = pygame.transform.rotate(image.copy(),-90)
        image = pygame.transform.flip(image.copy(),True,False)
    
        image2 = pygame.transform.scale(image.copy(),(r,r))
            
        im_rect = image2.get_rect()
            
        #place image at new location
        try:         
            self.screen.blit(image2,(int(x-im_rect.width/2),int(y - im_rect.height/2)))
            
        except ValueError:
            pass
    
        #Updates the display
        pygame.display.flip()
    
    def event(self):
        
        flags = self.key_controller.check_keys()
        return flags
        
    def stop_projecting(self):
        
        pygame.display.quit()
        pygame.quit()
