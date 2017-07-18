import cv2
import numpy as np
from WebcamInit import *

#Detector class has current x and y coordinates of the object
#There is room to implement techniques other than or in addition to detection
#note that there is a difference between detection and tracking
class Detector:
    #initializes x and y values to be referenced to by other classes

    
    #init uses all other functions to continuously compute current x and y
    def __init__(self):
        #readFramesHough function passes in self and the capture from
        #startCamera
        self.myCam = self.WebcamInit()
        self.x = 0
        self.y = 0
        self.radius = 0
        
        self.tracker = cv2.Tracker_create("MIL")
        self.bbox(200, 200, 200, 200)
        #bbox(center_x,center_y, radius*2, radius*2)
        self.ret = self.tracker.init(self.myCam.GetFrame().bbox)
    #uses hough circle transform to detect circles
    def getCoordinates(self):
        
        ret, frame = self.myCam.getFrame()
            
        ret, self.bbox = self.tracker.update(frame)
        
        return (self.bbox[0], self.bbox[1], self.bbox[2]/2)
        #return x, y, r

    def getFrame(self):
        
        return self.frame

    def stopRead(self):
        
        self.myCam.stopCam()
    

