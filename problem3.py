import cv2
import numpy as np
# 930 1990
# 1493 994
# 1519 994
# 2100 1990
track_original_image = cv2.imread('train_track.jpg')
track_resized_image = cv2.resize(track_original_image, (0, 0), fx = 0.5, fy = 0.5)
hieght = track_resized_image.shape[0]
width = int(track_resized_image.shape[1]/3)
# pts2 = np.float32([[465,995],[746,497],[760,497],[1050,995]])
pts1 = np.float32([[746,497],[760,497],[465,995],[1050,995]])
# pts1 = np.float32([[465,995],[465,497],[1050,497],[1050,995]])
pts2 = np.float32([[0,0],[width,0],[0, hieght],[width,hieght]])
homography_matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed_image = cv2.warpPerspective(track_resized_image, homography_matrix, (width, hieght))
cv2.circle(track_resized_image, (746,497), 3, (0,0,255), -1)
cv2.circle(track_resized_image, (760,497), 3, (0,0,255), -1)
cv2.circle(track_resized_image, (465,995), 3, (0,0,255), -1)
cv2.circle(track_resized_image, (1050,995), 3, (0,0,255), -1)
cv2.imshow('track resized image', track_resized_image)
cv2.imshow('transformed image', transformed_image)
cv2.waitKey(0)