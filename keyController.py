# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    projectImage for LightMap
'''

import pygame

#class to control projection.
#Escape, x, q  quit display
#Space         pause/start display

class keyController:
    
    def _init_(self,screen,paused):
        self.paused = paused = False
     
    def checkKeys():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            pygame.display.quit()
            #something else to restore the main gui
            #maybe stop recording here
            # maybe just return to main function 
        elif pressed[pygame.K_x]:
            pygame.display.quit()
        elif pressed[pygame.K_q]:
            pygame.display.quit()
        elif pressed[pygame.K_SPACE]:
            paused = (True, False)[paused]
        
            
            