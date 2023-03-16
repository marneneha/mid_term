import cv2
import numpy as np
import copy

baloon_original_image = cv2.imread('hotairbaloon.jpg')
baloon_resized_image = cv2.resize(baloon_original_image, (0, 0), fx = 0.2, fy = 0.2)
# cv2.imshow('original baloon image', baloon_original_image)
cv2.imshow('resized image', baloon_resized_image)
cv2.waitKey(0)
