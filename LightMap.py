#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ImageProcessing as ip
import cv2
    
class LightMap():
    def __init__(self, filename):
        img_pro = ip.ImageProcessing(filename)
        image = img_pro.file_sorting()
    
        for i in range(len(image)):
            cv2.imwrite("output{}.png".format(i), image[i])