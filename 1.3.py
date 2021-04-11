import numpy as np
import cv2 as cv

original = cv.imread("/home/pranjal/Desktop/pic1.jpg")
scale_percent = 30
width = int(original.shape[1] * scale_percent / 100)
height = int(original.shape[0] * scale_percent / 100)
dim = (width, height)
original = cv.resize(original, dim, None, fx = 10,fy=10)
blue = cv.cvtColor(original, cv.COLOR_BGR2RGB)
cv.imshow("Original", original)
cv.imshow("Blue", blue)
cv.waitKey(0)