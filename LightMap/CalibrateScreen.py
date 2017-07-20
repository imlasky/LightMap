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
import time
from scipy.interpolate import interp1d

class Calibrate:
    
    def __init__(self):
        
        self.x_offset = 0
        self.y_offset = 0
        self.coords_ind = 0
        self.x_locs = []
        self.y_locs = []
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.myKc = kc.KeyController(self.screen)
        self.detect = Detector.Detector()
        self.__calibrate()
        
        
    def __calibrate(self):
        
        # initialize quit and enter keys
        flags = self.myKc.check_keys()
        
        pygame.mouse.set_visible(False)
        
        w, h = self.screen.get_size()
        
    
        self.screen_width_space = np.linspace(50,w-50,50,dtype=np.uint16)
        self.screen_height_space = np.linspace(50,h-50,50,dtype=np.uint16)
        
        
        
        


        i = 0
        while True:
            
            self.screen.fill((0,0,0))
            
            pygame.draw.circle(self.screen,(255,0,0),(self.screen_width_space[i],self.screen_height_space[i]),50,5)
            pygame.display.flip()
            x_loc, y_loc, radius = self.detect.readFramesHough()
            
            
            self.x_locs.append(x_loc)
            self.y_locs.append(y_loc)
            flags = self.myKc.check_keys()

            i += 1    

            if flags[0] or i >= len(self.screen_width_space):
                self.radius = radius
                self.detect.stopRead()
                pygame.display.quit()
                pygame.quit()
                break
            
            time.sleep(0.2)
            
        
            
        self.detect.stopRead()
        self.__interp()
        pygame.display.quit()
        pygame.quit()

        
    def __interp(self):
        
        self.radius_ratio = self.radius/50
        
        self.fx = interp1d(self.x_locs,self.screen_width_space,bounds_error=False,
                           fill_value=0)
        
        self.fy = interp1d(self.y_locs,self.screen_height_space,bounds_error=False,
                           fill_value=0)
        
    def getOffsets(self,xold,yold):
        
        return self.fx(xold), self.fy(yold)
            
            