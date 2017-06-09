import cv2
import numpy as np
#import imutils
cv2.namedWindow("Trackfeed")
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while(True):
    #capture frame by frame
    ret, frame0 = cap.read()
    frame1 = cv2.medianBlur(frame0,15)
    #frame = imutils.resize(frame, width=600)
    #operations on frame come here
    frame2 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_GRAY2BGR)
    
    circles = cv2.HoughCircles(frame2,cv2.HOUGH_GRADIENT,1,120,
                            param1=100,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    
    if circles is None:
        cv2.imshow("Trackfeed", frame)
        continue
    
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
    
    cv2.imshow("Trackfeed",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
