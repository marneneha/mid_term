import cv2
import numpy as np
import copy
# 930 1990
# 1493 994
# 1519 994
# 2100 1990
track_original_image = cv2.imread('train_track.jpg')
track_resized_image = cv2.resize(track_original_image, (0, 0), fx = 0.5, fy = 0.5)
hieght = track_resized_image.shape[0]
width = int(track_resized_image.shape[1]/3)
# pts2 = np.float32([[465,995],[746,497],[760,497],[1050,995]])
pts1 = np.float32([[705,525],[807, 525],[500,700],[1008,700]])
# pts1 = np.float32([[465,995],[465,497],[1050,497],[1050,995]])
pts2 = np.float32([[0,0],[width,0],[0, hieght],[width,hieght]])
homography_matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed_image = cv2.warpPerspective(track_resized_image, homography_matrix, (width, hieght))
gray_transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_transformed_image, (57, 57), 0)
canny = cv2.Canny(gray_transformed_image, 200, 220, L2gradient =True)
lines = cv2.HoughLines(canny, 1, np.pi/180, 200)
# lines.pop()
lines = np.delete(lines, -1, 0)
for line in lines:
    # print("m here")
    # print(lines(line)[0][1])
    # if (line[0][1]-line[0][1])<0.1:
    #     print("m passing")
    #     break
    rho ,theta = line[0]
    a =np.cos(theta)
    b =np.sin(theta)
    x0 = (a * rho)
    y0 = (b * rho) 
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    transformed_image = cv2.line(transformed_image, [x1, y1], [x2, y2], [0,0,255], 1)
    print(transformed_image.shape)
    print(transformed_image[50,50])
    global first_point, second_point, dist
for row in range(transformed_image.shape[0]):
    second_point=0
    first_point=0
    dist=0
    for column in range(transformed_image.shape[1]):
        if(np.array_equal(transformed_image[row, column], np.array([0, 0, 255]))):
                # cv2.circle(transformed_image, (column, row), 2, (255, 0, 0), -1)
                # print("inside")
                # print(column)
                if(not first_point and not second_point):
                    first_point = copy.deepcopy(column)
                elif(first_point and not second_point and column != first_point):
                    second_point = copy.deepcopy(column)
                    dist = second_point-first_point
                    print("red detected")
                    print(dist)
                # print(first_point)
                # print(second_point)
                # print(dist)

cv2.imshow('canny', canny)
cv2.imshow('track resized image', track_resized_image)
cv2.imshow('transformed image', transformed_image)
cv2.waitKey(0)