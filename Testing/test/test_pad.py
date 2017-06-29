import cv2
import numpy as np
from distortion import *
import imutils
from loadImage import *
import pygame
from gui import GUI



#filename = GUI.returnFile()

stream = cv2.VideoCapture(0)
distort = DistortPicture()
distort.setCoeffs(0.2,0.0,0.0,0.0)
distort.setFocalLength(50,50)

if np.empty(filename):
     exit
im = ImportPicture(filename)
img = im.loadAsArray()

distort.setImage(img)

height, width = (540,960)
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()

while 1:
    
    
    _, frame = stream.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([150,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,None,iterations=2)
    
    contours = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(contours) > 0:
        
        max_c = max(contours, key=cv2.contourArea)
        
        ((x,y),radius) = cv2.minEnclosingCircle(max_c)     
        M = cv2.moments(max_c)
        
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        distort.setCenter(int(np.shape(img)[0] * y / height), int(np.shape(img)[1] * x / width))
        distort.setCameraMatrix()
        
        distorted = distort.distort()
        distorted = cv2.cvtColor(distorted,cv2.COLOR_BGR2RGB)
    
        img_d = im.convertToSurface(distorted)
        img_d = pygame.transform.scale(img_d,(2*int(radius),2*int(radius)))
        
        screen.fill((0,0,0))
        screen.blit(img_d,(int(x),int(y)))
    
        cv2.circle(frame,(int(x), int(y)), int(radius),  (0,255,255), 2)
        cv2.circle(frame,center,5,(0,0,255),-1)
    
    pygame.display.flip()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pygame.display.quit()
pygame.quit()
stream.release()
cv2.destroyAllWindows()
for i in range(0,4):
    cv2.waitKey(1)

