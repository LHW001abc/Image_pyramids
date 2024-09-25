import cv2 as cv
import numpy as np 

#link :https://docs.opencv.org/3.4/d4/d1f/tutorial_pyramids.html
#image pyramids
img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)


cv.imshow('Original Image', img)
cv.imshow('PyrDown1 Image', lr1)
cv.imshow('PyrDown2 Image', lr2)

#laplacian pyramid





cv.waitKey(0)
cv.destroyAllWindows()

