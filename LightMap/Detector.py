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
        self.my_camera = WebcamInit()
        self.x = 0
        self.y = 0
        self.radius = 0
        
    #uses hough circle transform to detect circles
    def read_frames_hough(self):
        
        self.frame0 = self.my_camera.getFrame()
        
        #blur to enhance detection abilities
        frame1 = cv2.medianBlur(self.frame0,5)

        #operations on frame come here
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
        #hough circles needs images to be in grayscale
        circles = cv2.HoughCircles(frame1,cv2.HOUGH_GRADIENT,1,120,
                            param1=100,param2=50,minRadius=20,maxRadius=200)
           
        #if circles are not detected, this is skipped. helps with efficiency
        if circles is not None:
            circles = np.uint16(np.around(circles))
            #draws circles
            for i in circles[0,:]:
                return i
        else:
            return (0,0,0)

    def get_frame(self):
        
        return self.frame0

    def stop_read(self):
        
        self.my_camera.stopCam()
    

