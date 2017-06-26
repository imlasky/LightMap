
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
        self.key = kc.KeyController()


        self.quitFlag = False
        
        
    def launch_app(self, user_input):
        self.detect = Detector.Detector()
        self.processed_images = self.images.file_sorting(user_input.filepath)
        self.processed_surface = []
        self.project = impr.ImageProjector()

#        cv2.imwrite("processed.jpg",self.processed_image[0][:,:,0:2])
        for i in range(0,len(self.processed_images)):
            
            self.processed_images[i] = self.image_surf.convertColor(self.processed_images[i].copy()[:,:,0:3])
            self.processed_surface.append(self.image_surf.convertToSurface(self.processed_images[i][:,:,0:3]))
        
        i = 0

        while True:
            i = i % len(self.processed_images)
            
            x, y, r = self.detect.readFramesHough()
            self.project.projectImage(self.processed_surface[i],x,y,r)
            
            i += 1
            exit_flag = self.project.check_keys()
            if exit_flag:
                break
        
        self.project.stopProjecting()
        self.detect.stopRead()
    
    
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = g.GUI()
    sys.exit(app.exec_())
