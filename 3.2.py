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
    #ret,frame = cv.threshold(frame,120,255,cv.THRESH_TRUNC )
    #frame = cv.medianBlur(frame,5)
    #ret,frame = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    
    
    frame = cv.adaptiveThreshold(frame, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,1)
    frame = cv.GaussianBlur(frame,(5,5),0)
    kernel = np.ones((5,5),np.uint8)
    #frame = cv.morphologyEx(frame, cv.MORPH_CLOSE, kernel)
    #frame = cv.dilate(frame,kernel,iterations = 1)
    #frame = cv.erode(frame,kernel,iterations = 1)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('a'):
        break