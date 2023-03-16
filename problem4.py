import cv2
import numpy as np
import copy

baloon_original_image = cv2.imread('hotairbaloon.jpg')
baloon_resized_image = cv2.resize(baloon_original_image, (0, 0), fx = 0.2, fy = 0.2)
gray_baloon_image = cv2.cvtColor(baloon_resized_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray_baloon_image, 5)
colored_blurred_baloon_image = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1,120, param1=200, param2=10, minRadius=0, maxRadius=100)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(baloon_resized_image, (i[0],i[1]), i[2], (0, 255, 0), -1)

# cv2.imshow('original baloon image', baloon_original_image)
cv2.imshow('resized image', baloon_resized_image)
cv2.waitKey(0)
