
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
from PyQt5.QtWidgets import *
import Gui as g

if __name__ != "__main__":
    import ImageProcessing as ip
    import DistortImage as di
    


    
class LightMap():   
    def __init__(self):
        self.images = ip.ImageProcessing()
        
        
    def launch_app(self, user_input):
    
        
        self.processed_image = self.images.file_sorting(user_input.filepath)
       
    #    detect()
        
    #def detect():
        
    #    (self.x,self.y,self.r) = DetectImage()
    
    
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = g.GUI()
    sys.exit(app.exec_())
