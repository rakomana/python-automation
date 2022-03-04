import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.imshow('Blank', blank)

#paint image a certain color
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#write text on the image
cv.putText(blank, 'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Blank', blank)

# this was for reading image
cv.waitKey(10000)