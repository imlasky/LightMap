import cv2
import numpy as np

#begins camera capture
cv2.namedWindow("Trackfeed")
cap = cv2.VideoCapture(0)



while(True):
    #capture frame by frame
    ret, frame0 = cap.read()
    frame1 = cv2.medianBlur(frame0,5)
    #frame = imutils.resize(frame, width=600)
    #operations on frame come here
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    
    circles = cv2.HoughCircles(frame1,cv2.HOUGH_GRADIENT,1,120,
                            param1=100,param2=50,minRadius=50,maxRadius=200)
    if (circles != None):
        
        circles = np.uint16(np.around(circles))
        
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame0,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame0,(i[0],i[1]),2,(0,0,255),3)
    
    
    
    
    
    cv2.imshow("Trackfeed",frame0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
