import numpy as np
import cv2 as cv

original = cv.imread("/home/pranjal/Desktop/pic1.jpg")
scale_percent = 30
width = int(original.shape[1] * scale_percent / 100)
height = int(original.shape[0] * scale_percent / 100)
dim = (width, height)
original = cv.resize(original, dim, None, fx = 10,fy=10)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
res, bw = cv.threshold(gray, 85, 255, cv.THRESH_BINARY, None)
cv.imshow("Original", original)
cv.imshow("Gray", gray)
cv.imshow("Black and White", bw)
cv.waitKey(0)