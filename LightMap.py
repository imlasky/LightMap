
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
from PyQt5.QtWidgets import *
import Gui as g

if __name__ != "__main__":
    import ImageProcessing as ip
    import DistortImage as di
    import Detector
    import ImageProjector as impr
    import VideoRecorder as vr
    
    


    
class LightMap():   
    def __init__(self):
        self.images = ip.ImageProcessing()
        self.quitFlag = False
        
        
    def launch_app(self, user_input):
        self.detect = Detector.Detector()
        self.processed_image = self.images.file_sorting(user_input.filepath)

        while !self.quitFlag:
            
            test = self.detect.readFramesHough()
            print(test[0],test[1],test[2])

        
        
        self.detect.stopRead()
    
    
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = g.GUI()
    sys.exit(app.exec_())
