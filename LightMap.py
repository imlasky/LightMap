
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import *
import Gui as g

if __name__ != "__main__":
    import ImageProcessing as ip
    import DistortImage as di
    import Detector
    import ImageProjector as impr
    import VideoRecorder as vr
    import ConvertImage as ci
    import KeyController as kc
    
    


    
class LightMap():   
    def __init__(self):
        self.images = ip.ImageProcessing()
        self.image_surf = ci.ConvertPicture()
        self.project = impr.ImageProjector()
        self.key = kc.KeyController()

        self.quitFlag = False
        
        
    def launch_app(self, user_input):
        self.detect = Detector.Detector()
        earth = cv2.imread("earth.jpg")
#        self.processed_image = self.images.file_sorting(user_input.filepath)
#        cv2.imwrite("processed.jpg",self.processed_image[0])
        self.processed_surface = self.image_surf.convertToSurface(earth)
        print(np.shape(earth))

        while True:
            test = self.detect.readFramesHough()
            self.project.projectImage(self.processed_surface,test[0],test[1],test[2])
            self.key.check_keys()
        
        
        self.detect.stopRead()
    
    
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = g.GUI()
    sys.exit(app.exec_())
