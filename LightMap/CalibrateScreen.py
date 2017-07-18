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
        self.xlocs = []
        self.ylocs = []
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1280,960))
        self.myKc = kc.KeyController(self.screen)
        self.detect = Detector.Detector()
        
        self.__calibrate()
        
        
    def __calibrate(self):
        
        # initialize quit and enter keys
        flags = self.myKc.check_keys()
        
        pygame.mouse.set_visible(False)
        
        w, h = self.screen.get_size()
        self.w = w
        self.h = h
        
        x_loc, y_loc, radius = self.detect.readFramesHough()
        
        
        frame = self.detect.getFrame()
        
        self.coords = np.array([[int(w/2),int(h/2)],[int(w/4),int(h/2)],[int(w/2),int(3*h/4)],
                   [int(3*w/4),int(h/2)],[w,int(h/2)],[int(w/2),h],[0,int(h/2)],[int(w/2),0]])
        
        w2, h2, _ = np.shape(frame)
        self.w2 = w2
        self.h2 = h2
        
        self.coords2 = np.array([[int(w2/2),int(h2/2)],[int(w2/4),int(h2/2)],[int(w2/2),int(3*h2/4)],
                   [int(3*w2/4),int(h2/2)],[w2,int(h2/2)],[int(w2/2),h2],[0,int(h2/2)]])     

        while True:
        
            
            #start with a black screen
            self.screen.fill((0,0,0))
        
            x_loc, y_loc, radius = self.detect.readFramesHough()
            
            
            im = pygame.image.load('../Images/Calibration.png')
            im = pygame.transform.scale(im,(50,50))
            im_rect = im.get_rect()
            im_rect.centerx = int(w/2)
            im_rect.centery = int(h/2)
            
            if im_rect:
                self.screen.blit(im,((self.coords[self.coords_ind,0]-int(im_rect.width/2)),self.coords[self.coords_ind,1]-int(im_rect.height/2)))
                if radius > 0:
                    pygame.draw.circle(self.screen,(255,255,0),(self.coords[self.coords_ind,0],self.coords[self.coords_ind,1]),radius,1)
            
            pygame.display.flip()
            flags = self.myKc.check_keys()
            if flags[1] and radius > 0:
                if self.coords_ind == 3:
                    self.xlocs.append(x_loc)
                    self.ylocs.append(y_loc)
                    self.x_offsets.append(self.coords2[self.coords_ind,0] - x_loc)
                    self.y_offsets.append(self.coords2[self.coords_ind,1] - y_loc)
                    break
                self.xlocs.append(x_loc)
                self.ylocs.append(y_loc)
                self.x_offsets.append(self.coords2[self.coords_ind,0] - x_loc)
                self.y_offsets.append(self.coords2[self.coords_ind,1] - y_loc)
                self.coords_ind += 1
            if flags[0]:
                self.detect.stopRead()
                pygame.display.quit()
                pygame.quit()
                return

        self.xlocs.append(self.w2)
        self.ylocs.append(int(self.h2/2))
        self.xlocs.append(int(self.w2/2))
        self.ylocs.append(self.h2)
        self.xlocs.append(0)
        self.ylocs.append(int(self.h2/2))
        self.xlocs.append(int(self.w2/2))
        self.ylocs.append(0)

        self.detect.stopRead()
        self.__interp()
        pygame.display.quit()
        pygame.quit()
        
    def __interp(self):
    

        
        #self.fx = interp1d(self.coords2[:,0]+self.x_offset,self.coords[:,0],bounds_error=False, fill_value=int(self.w/2))
        
        #self.fy = interp1d(self.coords2[:,1]+self.y_offset,self.coords[:,1],bounds_error=False, fill_value=int(self.h/2))
        
        self.fx = interp1d(self.xlocs,self.coords[:,0],bounds_error=False,fill_value=int(self.w/2))
        self.fy = interp1d(self.ylocs,self.coords[:,1],bounds_error=False,fill_value=int(self.h/2))
            
        print('Width: ' + str(self.w) + ' Height: ' + str(self.h))               
        print(str(self.coords2[:,0]))
        print(self.w2)
        
        
    def getOffsets(self,xold,yold):
        
        return self.fx(xold), self.fy(yold)
            
            
