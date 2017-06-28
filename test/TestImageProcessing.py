#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:33:13 2017

@author: dellwick
"""

import unittest
import ImageProcessing as ip
from unittest.mock import MagicMock
import cv2
import numpy as np
from PIL import Image

class NonanimatedTestCase(unittest.TestCase):
    def setUp(self):
        self.filepath = "test_1"
        
    def test_add_alpha(self):
        input_image = cv2.imread("test_1_crop_circle_0.png", 1)
        result_image = cv2.imread("test_1_add_alpha_0.png", -1)
        
        obj = ip.ImageProcessing()
        
        result = obj.add_alpha(input_image, 0)
        
        boolean = np.all(result == result_image)
        
        self.assertTrue(boolean)
        
        
    def test_trim_square(self):
        input_image = cv2.imread("test_1_pre_trim_square_0.png", 1)
        result_image = cv2.imread("test_1_trim_square_0.png", 1)
        
        obj = ip.ImageProcessing()
        
        center = 240, 320
        result = obj.trim_square(input_image, center, 240, 0)
        
        boolean = np.all(result == result_image)
        
        self.assertTrue(boolean) 
        
    def test_crop_circle(self):
        input_image = cv2.imread("test_1", 1)
        result_image = cv2.imread("test_1_crop_circle_0.png", 1)
        trim_square_result = cv2.imread("test_1_trim_square_0.png", 1)
        
    
        obj = ip.ImageProcessing()
        
        obj.get_size = MagicMock(return_value=(480, 640))
        obj.find_min = MagicMock(return_value=0)
        obj.trim_square = MagicMock(return_value=trim_square_result)
        
        result = obj.crop_circle(input_image, 0)
        
        boolean = np.all(result == result_image)
        
        self.assertTrue(boolean)  
        
    def test_generate_circle(self):
        input_image = cv2.imread("test_1", 1)
        
        image = []
        image.append(input_image)
        
        result_image = cv2.imread("test_1_generate_circle_0.png", -1)
        
        obj = ip.ImageProcessing()
        
        crop_circle_result = cv2.imread("test_1_crop_circle_0.png", 1)
        obj.crop_circle = MagicMock(return_value=crop_circle_result)
        
        add_alpha_result = cv2.imread("test_1_add_alpha_0.png", -1)
        obj.add_alpha = MagicMock(return_value=add_alpha_result)
        
        result = obj.generate_circle(image, 0)
        
        boolean = np.all(result == result_image)
        
        self.assertTrue(boolean) 
     
        
    def test_unanimated_image(self):
        result_image = cv2.imread("test_1_unanimated_image_0.png", -1)
        
        obj = ip.ImageProcessing()
        obj.filename = "test_1"
        
        generate_circle_result = cv2.imread("test_1_generate_circle_0.png", -1)
        obj.generate_circle = MagicMock(return_value=generate_circle_result)
        
        result = obj.unanimated_image()
        
        boolean = np.all(result == result_image)
        
        self.assertTrue(boolean)
        
    def test_image_processing(self):
        result_image = cv2.imread("test_1_image_processing_0.png", -1)
        
        obj = ip.ImageProcessing()
        
        unanimated_image_result = cv2.imread("test_1_generate_circle_0.png", -1)
        obj.generate_circle = MagicMock(return_value=unanimated_image_result)
        
        result = obj.image_processing("test_1")
        
        boolean = np.all(result == result_image)
        
        self.assertTrue(boolean)
        
    def test_get_size(self):
        image = cv2.imread("test_1", 1)
        
        obj = ip.ImageProcessing()
        
        dimensions = obj.get_size(image)
        
        self.assertEqual(dimensions, (480, 640))
        
    def test_find_min(self):
        x = [0, 1, 2]
        y = [1, 0, 2]
        result = [0, 1, 1]
        
        obj = ip.ImageProcessing()
        
        for i in range(len(result)):
            if obj.find_min(x[i], y[i]) != result[i]:
                self.assertTrue(False)
                
        self.assertTrue(True)      
        
class AnimatedTestCase(unittest.TestCase):
    def setUp(self):
        self.filepath = "test_2"
        self.frame_count = range(0, 6)
        
    def test_add_alpha(self):
        for i in self.frame_count:
            with self.subTest(i=i):
                input_image = cv2.imread("test_2_crop_circle_{}.png".format(i), 1)
                result_image = cv2.imread("test_2_add_alpha_{}.png".format(i), -1)
        
                obj = ip.ImageProcessing()
        
                result = obj.add_alpha(input_image, i)
        
                boolean = np.all(result == result_image)
        
                self.assertTrue(boolean)
 
    
    def test_trim_square(self):
        for i in self.frame_count:
            with self.subTest(i=i):
                input_image = cv2.imread("test_2_pre_trim_square_{}.png".format(i), 1)
                result_image = cv2.imread("test_2_trim_square_{}.png".format(i), 1)
                
                obj = ip.ImageProcessing()
                
                center = 106, 157
                result = obj.trim_square(input_image, center, 106, i)
                
                boolean = np.all(result == result_image)
                
                self.assertTrue(boolean) 
           
    def test_crop_circle(self):
        for i in self.frame_count:
            with self.subTest(i=i):
                input_image = cv2.imread("test_2_frame_{}.png".format(i), 1)
                result_image = cv2.imread("test_2_crop_circle_{}.png".format(i), 1)
                trim_square_result = cv2.imread("test_2_trim_square_{}.png".format(i), 1)
                
            
                obj = ip.ImageProcessing()
                
                obj.get_size = MagicMock(return_value=(212, 314))
                obj.find_min = MagicMock(return_value=0)
                obj.trim_square = MagicMock(return_value=trim_square_result)
                
                result = obj.crop_circle(input_image, i)
                
                boolean = np.all(result == result_image)
                
                self.assertTrue(boolean)  
                           
        
    def test_generate_circle(self):
        frames = [None]*6
        desired = [None]*6
        
        
        for i in self.frame_count:
            desired[i] = cv2.imread("test_2_generate_circle_{}.png".format(i), -1)
            
        obj = ip.ImageProcessing()
        
        for i in self.frame_count:
            with self.subTest(i=i):
                
                image = cv2.imread("test_2_crop_circle_{}.png".format(i), 1)
                obj.crop_circle = MagicMock(return_value=image)
                
                image = cv2.imread("test_2_add_alpha_{}.png".format(i), -1)
                obj.add_alpha = MagicMock(return_value=image)
        
                frame = obj.generate_circle(frames, i)
        
               
       
                boolean = np.all(frame == desired[i])
                
                if not boolean:
                    self.assertTrue(boolean)
         
        
        self.assertTrue(boolean)
    
    
    def test_get_size(self):
        obj = ip.ImageProcessing()
        
        for i in self.frame_count:
            with self.subTest(i=i):
                
                image = cv2.imread("test_2_frame_{}.png".format(i), 1)       
       
                dimensions = obj.get_size(image)
        
                self.assertEqual(dimensions, (212, 314))

    def test_animated_image(self):
        frames = []
        generated_frames = []
        expected = []
        
        
        for i in self.frame_count:
            generated_frames.append(cv2.imread("test_2_generate_circle_{}.png".format(i), -1))
            frames.append(cv2.imread("test_2_frame_{}.png".format(i), 1))
            expected.append(cv2.imread("test_2_animated_image_{}.png".format(i), -1))
        
        obj = ip.ImageProcessing()
        
        obj.filename = "test_2"
        
        obj.gif_divorce = MagicMock(return_value=frames)
        obj.generate_circle = MagicMock(side_effect=generated_frames)
        
        results = obj.animated_image()
        
        for i in self.frame_count:
            with self.subTest(i=i):
                boolean = np.all(results[i] == expected[i])
                
                if not boolean:
                    self.assertTrue(boolean)
                    
        self.assertTrue(boolean)
    
    def test_image_processing(self):
        for i in self.frame_count:
            with self.subTest(i=i):
                result_image = cv2.imread("test_2_image_processing_{}.png".format(i), -1)
                
                obj = ip.ImageProcessing()
                
                unanimated_image_result = cv2.imread("test_2_generate_circle_{}.png".format(i), -1)
                obj.generate_circle = MagicMock(return_value=unanimated_image_result)
                
                result = obj.image_processing("test_2")
                
                boolean = np.all(result == result_image)
                
                self.assertTrue(boolean)
    
    def test_gif_divorce(self):
        gif = Image.open("test_2")
        frames = []
        obj = ip.ImageProcessing()
        
        
        frames = obj.gif_divorce(gif)
        
        for i in self.frame_count:
            with self.subTest(i=i):
                comparable = cv2.imread("test_2_frame_{}.png".format(i), 1)
                
                boolean = np.all(comparable == frames[i])
                
                if not boolean:
                    self.assertTrue(boolean)
                    
        self.assertTrue(boolean)
        
        
    
    def test_find_min(self):
        x = [212, 314, 0, -1]
        y = [314, 212, 0, -2]
        result = [0, 1, 1, 1]
        
        obj = ip.ImageProcessing()
        
        for i in range(len(result)):
            if obj.find_min(x[i], y[i]) != result[i]:
                self.assertTrue(False)
                
        self.assertTrue(True)  
                  
    def test_get_frames(self):
        gif = Image.open("test_2")
        frames = []
        
        obj = ip.ImageProcessing()
        
        try:
            i = 0
            while True:
                gif.seek(i)
                imgframe = gif.copy()
                
                if i == 0:
                    palette = imgframe.getpalette()
                    
                else:
                    imgframe.putpalette(palette)
                    
                frames.append(imgframe)
                
                i += 1
                
        except EOFError:
            pass
    
        for i in self.frame_count:
            frames[i] = obj.get_frames(frames[i])
         
        for i in self.frame_count:
            comparable = cv2.imread("test_2_frame_{}.png".format(i), 1)
            
            if np.all(comparable != frames[i]):
                self.assertTrue(False)
                
        self.assertTrue(True)
        
if __name__ == "__main__":
    unittest.main()