#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Class: COP4331C (Summer 2017)
    Group: G13
    CalibrateScreen for LightMap
"""

import cv2
import numpy as np
import pygame
import KeyController as kc
import Detector

class Calibrate:
    
    def __init__(self):
        
        self.x_offset = 0
        self.y_offset = 0
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.myKc = kc.KeyController(self.screen)
        self.detect = Detector.Detector()
        self.__calibrate()
        
        
    def __calibrate(self):
        
        # initialize quit and enter keys
        flags = self.myKc.check_keys()
        
        pygame.mouse.set_visible(False)
        
        w, h = self.screen.get_size()


        while True:
            
            #start with a black screen
            self.screen.fill((0,0,0))
            
            x_loc, y_loc, radius = self.detect.readFramesHough()
            im = pygame.image.load('../Images/Calibration.png')
            im = pygame.transform.scale(im,(50,50))
            im_rect = im.get_rect()
            im_rect.centerx = int(w/2)
            im_rect.centery = int(h/2)
            
            self.screen.blit(im,(int(w/2)-int(im_rect.width/2),int(h/2)-int(im_rect.height/2)))
            if radius > 0:
                pygame.draw.circle(self.screen,(255,255,0),(int(w/2),int(h/2)),radius,1)
            
            pygame.display.flip()
            flags = self.myKc.check_keys()
            if flags[1] and radius > 0:
                break
            if flags[0]:
                self.detect.stopRead()
                pygame.display.quit()
                pygame.quit()
                return

        
        w2, h2, _ = np.shape(self.detect.getFrame())
        self.detect.stopRead()
        self.x_offset = int(w2/2) - x_loc
        self.y_offset = int(h2/2) - y_loc
        print(self.x_offset,self.y_offset)
        pygame.display.quit()
        pygame.quit()
        
    def getOffsets(self):
        
        return self.x_offset, self.y_offset
            
            