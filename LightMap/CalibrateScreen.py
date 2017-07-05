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
from scipy.interpolate import interp1d

class Calibrate:
    
    def __init__(self):
        
        self.x_offset = 0
        self.y_offset = 0
        self.coords_ind = 0
        self.x_offsets = []
        self.y_offsets = []
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.myKc = kc.KeyController(self.screen)
        self.detect = Detector.Detector()
        
        self.__calibrate()
        
        
    def __calibrate(self):
        
        # initialize quit and enter keys
        flags = self.myKc.check_keys()
        
        pygame.mouse.set_visible(False)
        
        w, h = self.screen.get_size()
        
        self.coords = [[int(w/2),int(h/2)],[int(w/4),int(h/2)],[int(w/2),int(3*h/4)],
                   [int(3*w/4),int(h/2)]]
        
        
        


        while True:
            
            #start with a black screen
            self.screen.fill((0,0,0))
            
            x_loc, y_loc, radius = self.detect.readFramesHough()
            im = pygame.image.load('../Images/Calibration.png')
            im = pygame.transform.scale(im,(50,50))
            im_rect = im.get_rect()
            im_rect.centerx = int(w/2)
            im_rect.centery = int(h/2)
            
            self.screen.blit(im,((self.coords[self.coords_ind][0]-int(im_rect.width/2)),self.coords[self.coords_ind][1]-int(im_rect.height/2)))
            if radius > 0:
                pygame.draw.circle(self.screen,(255,255,0),(self.coords[self.coords_ind][0],self.coords[self.coords_ind][1]),radius,1)
            
            pygame.display.flip()
            flags = self.myKc.check_keys()
            if flags[1] and radius > 0:
                if self.coords_ind == 3:
                    self.x_offsets.append(self.coords[self.coords_ind][0] - x_loc)
                    self.y_offsets.append(self.coords[self.coords_ind][1] - y_loc)
                    break
                self.x_offsets.append(self.coords[self.coords_ind][0] - x_loc)
                self.y_offsets.append(self.coords[self.coords_ind][1] - y_loc)
                self.coords_ind += 1
            if flags[0]:
                self.detect.stopRead()
                pygame.display.quit()
                pygame.quit()
                return

        
        self.detect.stopRead()
        self.__interp()
        pygame.display.quit()
        pygame.quit()
        
    def __interp(self):
        
#        f = interp1d(self.coords[:]1)
        
    def getOffsets(self):
        
        return self.x_offset, self.y_offset
            
            