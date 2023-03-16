import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
from cv_bridge import CvBridge

# print("inside project 1 file")
cap = cv2.VideoCapture('ball.mov')

if (cap.isOpened()==False):
    print("error on opening ")
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_frame, (5,5), 0) 
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=0, maxRadius=15) 
    if circles is not None:
        print("m here")
        circles = np.uint16(np.around(circles)) 
        chosen = circles[0,0]
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 0), 2)
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else: 
        break

# When everything done, release the video capture object
cap.release()
def main():
    pass
# Closes all the frames
cv2.destroyAllWindows()
if __name__ == '__main__':
    main()