import cv2 as cv

# reading images
img = cv.imread('images/faces.jpg')
# cv.imshow('Face', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Output", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    cv.imshow('Detected Faces', img)
# this was for reading image
cv.waitKey(0)