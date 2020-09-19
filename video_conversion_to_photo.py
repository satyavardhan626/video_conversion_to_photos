# Download python,cv2 from pip install opencv-python
# first Argument for function is video path
# Second Argument to function is the place we want to store images Extracted frpm the video
# run the file using command : python filename.py
# video will convert in to frames (1 sec = 30 frames)
# so for 1min video (60 secs * 30 = 1800 images)



import sys
import argparse

import cv2
print(".............",cv2.__version__)

def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print ('Read a new frame: ', success,image)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count += 1

extractImages(r"C:\Users\Downloads\REC_2020_07_12_03_25_24_F.MP4", r"C:\Users\Downloads\test")
