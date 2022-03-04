import cv2 as cv

# # reading images
img = cv.imread('images/user.png')

cv.imshow('Cat', img)

# flip
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

# # this was for reading image
cv.waitKey(0)