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