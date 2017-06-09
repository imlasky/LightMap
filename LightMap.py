#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:19:13 2017

@author: dellwick
"""

import ImageProcessing as ip
import gui_Tkinter as gui

if __name__ == "__main__":
    
    g = gui.GUI()
    
    img_pro = ip.ImageProcessing(g.fileChosen)
    
    image = img_pro.file_sorting()
    
