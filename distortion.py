import numpy as np
import cv2


        
cap = cv2.VideoCapture(0)

while 1:

    _, src = cap.read()
    
    width  = src.shape[1]
    height = src.shape[0]
    
    distCoeff = np.zeros((4,1),np.float64)
    
    k1 = 0.2; 
    k2 = 0.0;
    p1 = 0.0;
    p2 = 0.0;
    
    distCoeff[0,0] = k1;
    distCoeff[1,0] = k2;
    distCoeff[2,0] = p1;
    distCoeff[3,0] = p2;
    
    cam = np.eye(3,dtype=np.float32)
    
    cam[0,2] = width/2.0 - 100  # define center x
    cam[1,2] = height/2.0 + 100 # define center y
    cam[0,0] = 50.        # define focal length x
    cam[1,1] = 50.        # define focal length y
    
      # here the undistortion will be computed
    dst = cv2.undistort(src,cam,distCoeff)
    
    cv2.imshow('dst',dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
for i in range(0,4):
    cv2.waitKey(0)