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
    def __init__(self):
        self.size = ()
        
        
        
    # Sorts between animated and nonanimated images
    def file_sorting(self, filename):
        self.filename = filename
        
        animated_formats = ['gif']
        #, 'apng', 'mng', 'svg', 'svgz', 'webp']
        
        info = magic.from_file(self.filename, mime=True)
        info = info.split('/')
        
        if info[0] != 'image':
            raise TypeError("Application doesn't support this file format")
        
        elif info[1] not in animated_formats:
            return self.__unanimated_image()
            
        else:
            return self.__animated_image()
    
    # Handles all non animated file formats        
    def __unanimated_image(self):
        image = []
        
        image.append(cv2.imread(self.filename, 1))
        
        image[0] = self.__generate_circle(image[0])
        
        return image
            
    # Creates circular image with a transparent background
    def __generate_circle(self, image):
        image = self.__crop_circle(image)
        image = self.__add_alpha(image)
        
        #cv2.imwrite("output.png", image)
        return image
        
    
    # outlines the largest, center circle in the image  
    def __crop_circle(self, image):
        self.__get_size(image)
        index = self.__find_min(self.size[0], self.size[1])
        
        radius = floor(self.size[index] / 2)
        center = (floor(self.size[0] / 2), floor(self.size[1] / 2))
        
        
        circle = np.zeros(self.size, np.uint8)
        
        cv2.circle(circle, (center[1], center[0]), radius, 1, thickness=-1)
        
        image = cv2.bitwise_and(image, image, mask=circle)
        
        image = self.__trim_square(image, center, radius)
        
        return image
        
    # Crops the square surrounding the largest, centermost circle of the image 
    def __trim_square(self, image, center, radius):
        image = image[(center[0] - radius):(center[0] + radius),
                      (center[1] - radius):(center[1] + radius)]
    
        return image
        
        
    # Adds alpha layer behind circle image
    def __add_alpha(self, image):
        greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(greyscale, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(image)
        
        fourlayer = [b, g, r, alpha]
        return cv2.merge(fourlayer, 4)
        
        
    # Returns the number of the paramater of the shorter dimension
    def __find_min(self, x, y):
        if x < y:
            return 0
        else:
            return 1        
            
    # Gets the dimensions of the input image
    def __get_size(self, image):
        self.size = image.shape[:2]
        
        
    # Handles animated image formats 
    def __animated_image(self):
        #raise TypeError("Application doesn't support this file format")
        
        frames = []
        gif = Image.open(self.filename)
        
        for i, frame in enumerate(self.__gif_divorce(gif)):
            frame.save('temp.png', **frame.info)
            frames.append(cv2.imread('temp.png', 1))
            remove('temp.png')
            
            # list of png frames created
            
        for i in range(len(frames)):
            frames[i] = self.__generate_circle(frames[i])
            #cv2.imwrite("output%d.png" % i, frames[i])
            
        return frames
            
    # Breaks gif into frames and stores into list
    def __gif_divorce(self, gif):
        try:
            i = 0
            while True:
                gif.seek(i)
                imgframe = gif.copy()
                
                if i == 0:
                    palette = imgframe.getpalette()
                    
                else:
                    imgframe.putpalette(palette)
                    
                yield imgframe
                
                i += 1
                
        except EOFError:
            pass
                