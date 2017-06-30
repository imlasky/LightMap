# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    WebcamInit for LightMap
'''

import cv2
import numpy as np

class WebcamInit:
    
    def __init__(self):
        
        self.cap = cv2.VideoCapture(0)
        
    def getFrame(self):
        
        _, frame =  self.cap.read()
        return frame
    
    def stopCam(self):
        
        self.cap.release()
        for i in range(0,4):
            cv2.waitKey(1)