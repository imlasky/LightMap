"""
loadImage.py

Class allowing users to load images and convert between pygame surfaces and
numpy arrays easily

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
    
        
        