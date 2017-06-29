#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 23:19:05 2017

@author: dellwick
"""
import ImageProcessing as ip
import cv2
import unittest
from unittest.mock import MagicMock
import numpy as np

class FunctionalTestCase(unittest.TestCase):
    def test_nonanimated_image(self):
        filename = "test_1"
        
        obj = ip.ImageProcessing()
        result = obj.image_processing(filename)
        
        comparable = cv2.imread("test_1_unanimated_image_0.png", -1)
        
        state = np.all(comparable == result[0])
        
        self.assertTrue(state)
        
    def test_animated_image(self):
        filename = "test_2"
        
        obj = ip.ImageProcessing()
        result = obj.image_processing(filename)
        
        for i, res in enumerate(result):
            with self.subTest(i=i):
                comparable = cv2.imread("test_2_animated_image_{}.png".format(i), -1)
                
                state = np.all(comparable == res)
                
                self.assertTrue(state)

if __name__ == "__main__":
    unittest.main()
    
    