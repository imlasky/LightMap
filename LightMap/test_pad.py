
import cv2
import numpy as np
import ImageProcessing as ip

fname = "../Images/Earth.jpg"

myImage = ImageProcessing()

earth = myImage.file_sorting(fname)

cv2.imshow('Frame', earth);





