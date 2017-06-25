import cv2
import numpy as np


#Detector class has current x and y coordinates of the object
#There is room to implement techniques other than or in addition to detection
#note that there is a difference between detection and tracking
class Detector:
    #initializes x and y values to be referenced to by other classes
    x = 0
    y = 0
    radius = 0
    
    #init uses all other functions to continuously compute current x and y
    def __init__(self):
        #readFramesHough function passes in self and the capture from
        #startCamera
        self.readFramesHough(self, self.startCamera(self))
    
    #begins live video capture from webcam, returns this as 'cap'
    def startCamera(self):
        cv2.namedWindow("Trackfeed")
        cap = cv2.VideoCapture(0)
        return cap

    #uses hough circle transform to detect circles
    def readFramesHough(self, cap):
        while(True):
            #loop thats captures frame by frame
            ret, frame0 = cap.read()
            
            #blur to enhance detection abilities
            frame1 = cv2.medianBlur(frame0,5)

            #operations on frame come here
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
            #hough circles needs images to be in grayscale
            circles = cv2.HoughCircles(frame1,cv2.HOUGH_GRADIENT,1,120,
                            param1=100,param2=50,minRadius=50,maxRadius=200)
           
            #if circles are not detected, this part is skipped. helps with
            #efficiency
            if (circles != None):
                
                
                circles = np.uint16(np.around(circles))
        
                #draws circles
                for i in circles[0,:]:
                    # draw the outer circle
                    cv2.circle(frame0,(i[0],i[1]),i[2],(0,255,0),2)
                    # draw the center of the circle
                    cv2.circle(frame0,(i[0],i[1]),2,(0,0,255),3)
                    #records center of circle and changes the coordinates
                    #and radius
                    Detector.x = i[0]
                    Detector.y = i[1]
                    Detector.radius = i[2]
    
            cv2.imshow("Trackfeed",frame0)
            #quits on q, I've had trouble with this on my machine where I need
            #to force quit and it has extrenous bytes
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
