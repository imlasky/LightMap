#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:42:18 2017

@author: Zachary Freer
"""

import magic
import cv2
import numpy as np
from PIL import Image
from math import floor
from os import remove


# Differentiates from animated and nonanimated image formats and crops them 
# into a circle with an alpha layer in the background.
class ImageProcessing():
    def __init__(self, filename):
        self.filename = filename
        self.size = ()
        
    # Sorts between animated and nonanimated images
    def file_sorting(self):
        animated_formats = ['gif', 'apng', 'mng', 'svg', 'svgz', 'webp']
        
        info = magic.from_file(self.filename, mime=True)
        info = info.split('/')
        
        if info[0] != 'image':
            raise TypeError("Application doesn't support this file format")
        
        elif info[1] not in animated_formats:
            return self.unanimated_image()
            
        else:
            return self.animated_image()
    
    # Handles all non animated file formats        
    def unanimated_image(self):
        image = []
        
        image.append(cv2.imread(self.filename, 1))
        
        image[0] = self.generate_circle(image[0])
        
        return image
            
    # Creates circular image with a transparent background
    def generate_circle(self, image):
        image = self.crop_circle(image)
        image = self.add_alpha(image)
        
        #cv2.imwrite("output.png", image)
        return image
        
    
    # outlines the largest, center circle in the image  
    def crop_circle(self, image):
        self.get_size(image)
        index = self.find_min(self.size[0], self.size[1])
        
        radius = floor(self.size[index] / 2)
        center = (floor(self.size[0] / 2), floor(self.size[1] / 2))
        
        
        circle = np.zeros(self.size, np.uint8)
        
        cv2.circle(circle, (center[1], center[0]), radius, 1, thickness=-1)
        
        image = cv2.bitwise_and(image, image, mask=circle)
        
        image = self.trim_square(image, center, radius)
        
        return image
        
    # Crops the square surrounding the largest, centermost circle of the image 
    def trim_square(self, image, center, radius):
        image = image[(center[0] - radius):(center[0] + radius),
                      (center[1] - radius):(center[1] + radius)]
    
        return image
        
        
    # Adds alpha layer behind circle image
    def add_alpha(self, image):
        greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(greyscale, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(image)
        
        fourlayer = [b, g, r, alpha]
        return cv2.merge(fourlayer, 4)
        
        
    # Returns the index of the shorter dimension of the input image
    def find_min(self, x, y):
        if x < y:
            return 0
        else:
            return 1        
            
    # Gets the dimensions of the input image
    def get_size(self, image):
        self.size = image.shape[:2]
        
        
    # Handles animated image formats 
    def animated_image(self):
        raise TypeError("Application doesn't support this file format")
        
            
    # Breaks gif into frames and stores into list
    def gif_divorce(self, gif):
        pass
                
