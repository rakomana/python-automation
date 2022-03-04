import cv2 as cv

# reading images
image = cv.imread('images/user.png')
img = cv.resize(image, (500,500))
cv.imshow('Original', img)

# converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilate', dilated)

# this was for reading image
cv.waitKey(0)