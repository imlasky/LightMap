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

class ImageProcessing():
    def __init__(self):
        self.filename = ""
        np.set_printoptions(threshold=np.inf)
    
    def image_processing(self, filename):
        self.filename = filename
        
        animated_formats = ['gif']
        
        info = magic.from_file(self.filename, mime=True)
        info = info.split('/')
        
        if info[0] != 'image':
            raise TypeError("Application doesn't support this file format")
        
        elif info[1] not in animated_formats:
            cropped_images = self.unanimated_image()
            
        else:
            cropped_images = self.animated_image()
        
        return cropped_images
           
    def unanimated_image(self):
        image = []
        
        image.append(cv2.imread(self.filename, 1))
        
        image = self.generate_circle(image)
    
        return image
            
    # Creates circular image with a transparent background
    def generate_circle(self, image, frame_number):

        image = self.crop_circle(image, frame_number)
        
        image = self.add_alpha(image, frame_number)
           
        return image

    # outlines the largest, center circle in the image  
    def crop_circle(self, image, frame_number):
        dimensions = self.get_size(image)
        index = self.find_min(dimensions[0], dimensions[1])
        
        radius = floor(dimensions[index] / 2)
        center = (floor(dimensions[0] / 2), floor(dimensions[1] / 2))
        
        circle = np.zeros(dimensions, np.uint8)
        
        cv2.circle(circle, (center[1], center[0]), radius, 1, thickness=-1)
        
        image = cv2.bitwise_and(image, image, mask=circle)
        
        image = self.trim_square(image, center, radius, frame_number)
        
        return image
        
    # Crops the square surrounding the largest, centermost circle of the image 
    def trim_square(self, image, center, radius, frame_number):
        image = image[(center[0] - radius):(center[0] + radius),
                      (center[1] - radius):(center[1] + radius)]
          
        return image
        
        
    # Adds alpha layer behind circle image
    def add_alpha(self, image, frame_number):
        greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(greyscale, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(image)
        
        fourlayers = [b, g, r, alpha]
        
        image = cv2.merge(fourlayers, 4)
        
        return image
        
        
    # Returns the number of the paramater of the shorter dimension
    def find_min(self, x, y):
        if x < y:
            return 0
        else:
            return 1        
            
    # Gets the dimensions of the input image
    def get_size(self, image):
        size = image.shape[:2]
        return size
 
    def animated_image(self):
        frames = []
        
        gif = Image.open(self.filename)
        
        gif_frames = self.gif_divorce(gif)

        for i in range(len(gif_frames)):    
            image = self.generate_circle(gif_frames[i], i)
            frames.append(image)
            
        return frames
    
    def get_frames(self, frame_info):
        frame_info.save('temp.png', **frame_info.info)
        frame = cv2.imread('temp.png', 1)
        remove('temp.png')
        
        return frame
    
    def gif_divorce(self, gif):
        frames = []
        try:
            i = 0
            while True:
                gif.seek(i)
                imgframe = gif.copy()
                
                if i == 0:
                    palette = imgframe.getpalette()
                    
                else:
                    imgframe.putpalette(palette)
                    
                current_frame = self.get_frames(imgframe)
                
                frames.append(current_frame)
        
                i += 1
                
        except EOFError:
            return frames