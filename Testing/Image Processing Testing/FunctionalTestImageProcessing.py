#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 23:19:05 2017

@author: dellwick
"""
import ImageProcessing as ip
import cv2

'''
test_1 is a png 
Desired output should be a square image with a circular colored area centered
Output saved as "result0.0.png"

test_2 is a six-frame gif
Desired output should be six square images with a circular colored area centered
Output saved as "result1.0.png", "result1.1.png", "result1.2.png",
                "result1.3.png", "result1.4.png", "result1.5.png"
'''

def main():
    images = []
    images.append("test_1")
    images.append("test_2")
    
    processing = ip.ImageProcessing()
    
    for i in range(len(images)):
        
        image = processing.image_processing(images[i])
        
        for j in range(len(image)):
            cv2.imwrite("result{}.{}.png".format(i, j), image[j])

if __name__ == "__main__":
    main()
    
    