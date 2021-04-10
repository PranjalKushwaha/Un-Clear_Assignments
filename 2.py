import numpy as np
import cv2 as cv

original = cv.imread("/home/pranjal/Pictures/sample.png")
scale_percent = 300
width = int(original.shape[1] * scale_percent / 100)
height = int(original.shape[0] * scale_percent / 100)
dim = (width, height)
original = cv.resize(original, dim, None, fx = 10,fy=10)
#blurs
blur1 = cv.blur(original, (5,5))
blur2 = cv.GaussianBlur(original, (7,7),0)
#translation
rows,cols,s = original.shape
k = np.float32([[1,0,100],[0,1,100]])
tra1 = cv.warpAffine(original,k,(cols,rows))
k = np.float32([[1,0,100],[0,1,-100]])
tra2 = cv.warpAffine(original,k,(cols,rows))
k = np.float32([[1,0,-100],[0,1,100]])
tra3 = cv.warpAffine(original,k,(cols,rows))
k = np.float32([[1,0,-100],[0,1,-100]])
tra4 = cv.warpAffine(original,k,(cols,rows))
#rotation
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),30,1)
rot1 = cv.warpAffine(original,M,(cols,rows))
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),60,1)
rot2 = cv.warpAffine(original,M,(cols,rows))
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
rot3 = cv.warpAffine(original,M,(cols,rows))
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),180,1)
rot4 = cv.warpAffine(original,M,(cols,rows))


cv.imshow("Box_Blur", blur1)
cv.imshow("Gaussian Blur", blur2)
cv.imshow("Original", original)
cv.imshow("Translation 1", tra1)
cv.imshow("Translation 2", tra2)
cv.imshow("Translation 3", tra3)
cv.imshow("Translation 4", tra4)
cv.imshow("Rotation 1", rot1)
cv.imshow("Rotation 2", rot2)
cv.imshow("Rotation 3", rot3)
cv.imshow("Rotation 4", rot4)

cv.waitKey(0)