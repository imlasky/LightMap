"""
loadImage.py

Class allowing users to load images and convert between pygame surfaces and
numpy arrays easily

"""

import numpy as np
import pygame
import cv2

class ConvertImage:

    def convert_color(self,array):
        
        self.array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
        return self.array
    
    def convert_to_surface(self,array):
        
        self.surface = pygame.surfarray.make_surface(array)
        return self.surface
    
    def convert_to_array(self,surface):
        
        self.array = pygame.surfarray.pixels3d(surface)
        return self.array
    
        
        