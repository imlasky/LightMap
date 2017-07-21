
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys
from PyQt5.QtWidgets import *
import Gui as g

if __name__ != "__main__":
    import ImageProcessing as ip
    import Detector
    import ImageProjector as impr
    import ConvertImage as ci
    import CalibrateScreen as cs
    
class LightMap():   
    def __init__(self):
        self.images = ip.ImageProcessing()
        self.image_surface = ci.ConvertImage()
        
    def launch_app(self, user_input):
        self.calibration = cs.Calibrate()
        self.detector = Detector.Detector()
        self.processed_surface = []
        self.radii = []
        self.image_projector = impr.ImageProjector()
        self.offset_x = 0
        self.offset_y = 0


        self.processed_images = self.images.image_processing(user_input.filepath)


        for i in range(0,len(self.processed_images)):
            
            self.processed_images[i] = self.image_surface.convert_color(self.processed_images[i].copy()[:,:,0:3])
            self.processed_surface.append(self.image_surface.convert_to_surface(self.processed_images[i][:,:,0:3]))
        
        frame_number = 0
        radius_index = 0
        
        
        while True:
        
            radius_index %= 10
            frame_number = frame_number % len(self.processed_images)
            
            x_loc, y_loc, radius = self.detector.read_frames_hough()
            
            if len(self.radii) < 10:
                self.radii.append(radius)
            else:
                self.radii[radius_index] = radius
                
            new_radius = np.average(self.radii)
            
            self.offset_x, self.offset_y = self.calibration.get_offsets(x_loc,y_loc)
            self.radius = self.calibration.get_radius(new_radius)

            
            
#           
            self.image_projector.project_image(self.processed_surface[frame_number],self.offset_x-375,self.offset_y-185,int(self.radius))
            
            frame_number += 1
            radius_index += 1
            flags = self.image_projector.event()
            
            if flags[0]:
                break
        
        self.image_projector.stop_projecting()
        self.detector.stop_read()
  
        
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = g.GUI()
    sys.exit(app.exec_())
