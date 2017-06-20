# -*- coding: utf-8 -*-
'''
    Class: COP4331C (Summer 2017)
    Group: G13
    recordVideo for LightMap
'''

import cv2
import os

class recordVideo:
    
    
    def __init__(self,filename):
        # Define the codec and create VideoWriter object
        #The 'DIVX' codex format works for Windows and Linux
        fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
        #This works when filename is in the form "filename.avi" 
        self.out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))
    
        
        #this should be used to store the frame before distortion and analysis
    def recordFrame(self,frame):
        #flip the frame
        frame = cv2.flip(frame,0)
        # write the flipped frame
        self.out.write(frame)
        return
    
    #this is meant as utility for the gui to validate filename 
    #returns true if file doesn't exist so we can safely open filename
    @staticmethod
    def canOpenFile(self,filename):
        return not os.path.exists(filename)
   
        

