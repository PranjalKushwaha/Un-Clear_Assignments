import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)

while True:
    r, frame = vid.read()
    scale_percent = 200
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv.resize(frame, dim, None, fx = 10,fy=10)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    frame = cv.adaptiveThreshold(frame, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,1)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('a'):
        break