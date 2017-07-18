#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:32:32 2017
@author: eebz
"""

class InputValues:
    def __init__(self):
        
        
        self.filepath = ""
        
        self.record_video = False
        
#        self.mapping_status = False
        
        
        
        
    def update_values(self, filepath, record_video):
        

        
        self.filepath = filepath
        
        self.record_video = record_video
        
#        self.mapping_status = mapping_status
        
    
