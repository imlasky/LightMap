# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:02:50 2017

@author: Alec
"""

import ImageProjector
import pygame
import time

#Start of testing
if __name__ == "__main__":
    
    project = ImageProjector.ImageProjector()
    
    #hopefully this will resize the screen the projector made
    height, width = (1080,1920)
    size = (width, height)
    screen = pygame.display.set_mode(size)
    
    earth = pygame.image.load("earth.jpg")
    
    project.projectImage(earth,250,250,50)
    
    #will stall execution for 30 seconds
    time.sleep(30)
    pygame.display.quit()
    pygame.quit()