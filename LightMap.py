#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ImageProcessing as ip
import DistortImage as di
import cv2
from gui import *
    
class LightMap():
    def __init__(self, filename):
        
        self.filename = filename
        self.img_pro = ip.ImageProcessing(self.filename)
        self.images = self.img_pro.file_sorting()
        
        detect()
        
    def detect():
        
        (self.x,self.y,self.r) = DetectImage()
    
    
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
