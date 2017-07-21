
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
    import Tracker
    import ImageProjector as impr
    import VideoRecorder as vr
    import ConvertImage as ci
    import KeyController as kc
    import CalibrateScreen as cs
    
    


    
class LightMap():   
    def __init__(self):
        self.images = ip.ImageProcessing()
        self.image_surf = ci.ConvertPicture()
        
    def launch_app(self, user_input):
        self.calib = cs.Calibrate()
        self.detect = Detector.Detector()
        #self.track = Tracker.Tracker()
        self.processed_surface = []
        self.radii = []
        self.project = impr.ImageProjector()
        self.video = vr.VideoRecorder('output.avi')
        self.offset_x = 0
        self.offset_y = 0


        self.processed_images = self.images.image_processing(user_input.filepath)


        for i in range(0,len(self.processed_images)):
            
            self.processed_images[i] = self.image_surf.convertColor(self.processed_images[i].copy()[:,:,0:3])
            self.processed_surface.append(self.image_surf.convertToSurface(self.processed_images[i][:,:,0:3]))
        
        frame = 0
        rad_ind = 0
        
        
        while True:
        
            rad_ind %= 10
            frame = frame % len(self.processed_images)
            
            x_loc, y_loc, radius = self.detect.readFramesHough()
            
            if len(self.radii) < 10:
                self.radii.append(radius)
            else:
                self.radii[rad_ind] = radius
                
            new_radius = np.average(self.radii)
            
            self.offset_x, self.offset_y = self.calib.getOffsets(x_loc,y_loc)
            self.radius = self.calib.getRadius(new_radius)

            
#            if user_input.record_video:
#                self.video.record_frame(self.detect.getFrame())
        
            self.project.projectImage(self.processed_surface[frame],self.offset_x-375,self.offset_y-185,int(self.radius))
            
            frame += 1
            rad_ind += 1
            flags = self.project.event()
            
            if flags[0]:
                break
        
        self.project.stopProjecting()
        self.detect.stopRead()
  
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = g.GUI()
    sys.exit(app.exec_())
