#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:31:00 2017

@author: ian
"""

import numpy as np
import cv2
import pygame
from wand.image import Image
from wand.display import display
import time

#with Image(filename='checker.png') as earth:
#    with earth.clone() as earth_d:
#        for i in np.arange(-0.5,0.5,0.05):
#            earth_d.distort('barrel',(i,0,0.0,1.0))
#            earth_d.save(filename='checker_d.png')            
##            cv2.imshow('earth',earth_d)
##            time.sleep(100)




                         

cap = cv2.VideoCapture(0)



height, width = (600,800)

size = (width, height)

screen = pygame.display.set_mode(size)

pygame.init()

earth = pygame.image.load("earth.jpg")

#moon = []
#for i in range(0,238):
#    moon.append(pygame.image.load('./moon/frame_'+str(i)+'_delay-0.04s.gif'))
#
#print(len(moon))
#for i in range(0,238):
#    moon[i] = pygame.image.load('/home/ian/Documents/COP4331/detection/moon/frame_'+str(i)+'_delay-0.04s.gif')



#tmp = np.zeros_like(img)
#alpha = np.zeros_like(img)
#
#tmp = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#_,alpha = cv2.threshold(tmp,10,255,cv2.THRESH_BINARY)
#
#r,g,b = cv2.split(img)
#
#
#
#rgba = cv2.merge((r,g,b,alpha))
#
#
#rgba = cv2.resize(rgba,(int(0.5*rgba.shape[0]),int(0.2*rgba.shape[1])),interpolation=cv2.INTER_LINEAR)
#
#cv2.imwrite('rgba.png',rgba)
#rgba = cv2.imread('rgba.png')

#rgba = np.array(rgba)

cnt = 0
while 1:
    _, frame = cap.read()
    cnt = cnt%238

    #cv2.bitwise_and(frame,rgba)
#    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#    
#
#    lower_blue = np.array([90,50,50])
#    upper_blue = np.array([150,255,255])
#
#    mask = cv2.inRange(hsv,lower_blue,upper_blue)
#    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,None,iterations=2)
    
    

    frame = cv2.medianBlur(frame,5)
    gframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gframe,cv2.HOUGH_GRADIENT,1,50,
                            param1=30,param2=65,minRadius=0,maxRadius=0)
    
    if circles != None:
    
        circles = np.uint16(np.around(circles))
    
#    contours = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
#    center = None
#    if len(contours) > 0:
#        max_c = max(contours, key=cv2.contourArea)
        #max_c = max(cv2.arcLength(circles,True))
        for i in circles[0,:]:
            
        
#        ((x,y),radius) = cv2.minEnclosingCircle(max_c)
##        
##        
#        M = cv2.moments(max_c)
#
#        
#        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
#        if radius > 5:
#            earth_temp = earth.copy()
#            earth_temp = pygame.transform.scale(earth_temp,(2*int(radius),2*int(radius)))
##            moon_temp = moon[cnt].copy()
##            moon_temp = pygame.transform.scale(moon_temp,(2*(int(radius)),2*(int(radius))))
#            screen.fill((0,0,0))
#            screen.blit(earth_temp,(int(x),int(y)))
#    
#            #screen.blit(moon_temp,(int(1920*x/frame.shape[1]),int(1080*y/frame.shape[0])))
#            cv2.circle(frame,(int(x), int(y)), int(radius),  (0,255,255), 2)
#            cv2.circle(frame,center,5,(0,0,255),-1)
            
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
     #draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            earth_temp = earth.copy()
            earth_temp = pygame.transform.scale(earth_temp,(2*int(i[2]),2*int(i[2])))
            screen.fill((0,0,0))
            screen.blit(earth_temp,(i[0],i[1]))
            
    cnt = cnt + 1
    pygame.display.flip()
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
pygame.display.quit()
pygame.quit()
cap.release()
cv2.destroyAllWindows()
for i in range(0,4):
    cv2.waitKey(1)