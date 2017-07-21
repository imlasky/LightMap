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
        
        self.x_locations = []
        self.y_locations = []
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.key_controller = kc.KeyController(self.screen)
        self.detector = Detector.Detector()
        self.__calibrate()
        
        
    def __calibrate(self):
        
        # initialize quit and enter keys
        flags = self.key_controller.check_keys()
        
        pygame.mouse.set_visible(False)
        
        w, h = self.screen.get_size()
        
        circ_rad = 75
        num_points = 25
        
    
        self.screen_width_space = np.linspace(circ_rad,w-circ_rad,num_points,dtype=np.uint16)
        self.screen_height_space = np.linspace(circ_rad,h-circ_rad,num_points,dtype=np.uint16)
        
        down_right_complete = 0
        up_left_complete = 0

        i = 0
        while True:
            
            self.screen.fill((0,0,0))
            
            #if not down_right_complete:
            pygame.draw.circle(self.screen,(255,255,255),(self.screen_width_space[i],
                               self.screen_height_space[i]),circ_rad,10)
      
            pygame.display.flip()
            x_loc, y_loc, radius = self.detector.read_frames_hough()
            
            if radius > 0:
                self.x_locations.append(x_loc)
                self.y_locations.append(y_loc)
                self.radius = radius
                i += 1 
            
            time.sleep(0.6)       
            flags = self.key_controller.check_keys()
            if flags[0] or i >= len(self.screen_width_space):
                break
   
        self.detector.stop_read()
        self.__interp(circ_rad)
        pygame.display.quit()
        pygame.quit()

        
    def __interp(self,rad):
        
        self.radius_ratio = self.radius/rad
        
        self.fx = interp1d(self.x_locations,self.screen_width_space,bounds_error=False,
                           fill_value=0)
        
        self.fy = interp1d(self.y_locations,self.screen_height_space,bounds_error=False,
                           fill_value=0)
        
    def get_offsets(self,xold,yold):
        
        return self.fx(xold), self.fy(yold)
    
    def get_radius(self,radiusold):
        
        #return radiusold/self.radius_ratio
        return 6*radiusold
            
            
