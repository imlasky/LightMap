#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:32:32 2017

@author: eebz
"""

class InputValues:
    def setValues(self,projectorDist,cameraDist,projectorHeight,cameraHeight):
        
        self.projectorDistance = projectorDist
        self.cameraDistance = cameraDist
        self.projectorHeight = projectorHeight
        self.cameraHeight = cameraHeight
        
    def getProjectorDistance(self):
        
        return self.projectorDistance
    
    def getCameraDistance(self):
        
        return self.cameraDistance
        
    def getProjectHeight(self):
        
        return self.projectorHeight
    
    def getCameraHeight(self):
        
        return self.cameraHeight
        