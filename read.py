# import cv2 as cv

# # reading images
# # img = cv.imread('images/user.png')

# # cv.imshow('Cat', img)

# # this was for reading image
# # cv.waitKey(0)
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Output", gray)
    else:
        break
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()