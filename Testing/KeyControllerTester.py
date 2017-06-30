# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:08:51 2017

@author: Alec
"""
import ImageProjector
import KeyController
import time
import pygame

class KeyControllerTestHelper:
    
    #Will run for 2 minutes while keys are pressed and print a message for each flag recieved 
    # returns number of keys pressed while testing
    @staticmethod
    def DoesItWork():
        key = 0 
        
        #This sets the time limit to min 
        endtime = time.time() + 60 * 1
        
        project = ImageProjector.ImageProjector()
    
        #hopefully this will resize the screen the projector made
        height, width = (1080,1920)
        size = (width, height)
        screen = pygame.display.set_mode(size)
    
        earth = pygame.image.load("earth.jpg")
        
        project.projectImage(earth,250,250,50)
        
        while time.time() < endtime:
            x,y = project.myKc.check_keys()
            
            if x:
                print "Yay, exit flag was raised"
                break
                
            if y:
                print "Yay, enter flag was raised"
                break



#Start of testing
if __name__ == "__main__":
    pygame.init()
    KeyControllerTestHelper.DoesItWork()
    pygame.quit()
        
        
