#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:32:32 2017
@author: eebz
"""

class InputValues:
    def __init__(self):
        self.projector_height = -1.0
        self.projector_distance = -1.0
        
        self.camera_height = -1.0
        self.camera_distance = -1.0
        
        self.filepath = ""
        
        self.record_video = False
        
#        self.mapping_status = False
        
        
        
        
    def update_values(self, hardware_positions, filepath, record_video):
        
        self.projector_height = hardware_positions[0]
        self.projector_distance = hardware_positions[1]
        
        self.camera_height = hardware_positions[2]
        self.camera_distance = hardware_positions[3]
        
        self.filepath = filepath
        
        self.record_video = record_video
        
#        self.mapping_status = mapping_status
        
    
