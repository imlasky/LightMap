#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:12:37 2017

@author: ian
"""

import numpy as np
import pygame
import cv2

class ImportPicture:
            
    def __init__(self,filename):
        
        self.filename = filename
        
    def loadAsSurface(self):
        
        self.surface = pygame.image.load(self.filename)
        return self.surface
    
    def loadAsArray(self):
        
        self.array = cv2.imread(self.filename)
        return self.array
    
    def convertToSurface(self,array):
        
        self.surface = pygame.surfarray.make_surface(array)
        return self.surface
    
    def convertToArray(self,surface):
        
        self.array = pygame.surfarray.pixels3d(surface)
        return self.array
    
        
        