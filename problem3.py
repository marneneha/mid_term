import cv2
import numpy as np
# 930 1990 1000 1400
# 1493 994 1410 1050
# 1519 994 1614 1050 
# 2100 1990 2016 1400
def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("U-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 0, 255, nothing)
cv2.setTrackbarPos("L-H", "Trackbars", 179)
cv2.setTrackbarPos("L-S", "Trackbars", 255)
cv2.setTrackbarPos("L-V", "Trackbars", 255)
global hsv, track_original_image, track_resized_image, transformed_image, homography_matrix
while True:
    track_original_image = cv2.imread('train_track.jpg')
    track_resized_image = cv2.resize(track_original_image, (0, 0), fx = 0.5, fy = 0.5)
    hieght = track_resized_image.shape[0]
    width = int(track_resized_image.shape[1]/3)
    pts1 = np.float32([[705,525],[807, 525],[500,700],[1008,700]])
    pts2 = np.float32([[0,0],[width,0],[0, hieght],[width,hieght]])
    homography_matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_image = cv2.warpPerspective(track_resized_image, homography_matrix, (width, hieght))
    hsv = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2HSV)
    lower_mask_limit = np.array([0, 100, 100])
    upper_mask_limit = np.array([2, 255, 255])
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    lower_mask_limit = np.array([100, 100, 100])
    upper_mask_limit = np.array([150, 200, 200])
    print(lower_mask_limit)
    print(upper_mask_limit)
    mask = cv2.inRange(hsv, lower_mask_limit, upper_mask_limit)
    result = cv2.bitwise_and(transformed_image, transformed_image, mask=mask)
    cv2.imshow('track resized image', track_resized_image)
    cv2.imshow('transformed image', transformed_image)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    key = cv2.waitKey(1)
    if key == 'k':
        break