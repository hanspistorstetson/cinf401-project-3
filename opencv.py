import cv2
import sys
import numpy as np

image = cv2.imread(sys.argv[1])
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(gray, kernel, iterations = 1)
dilation = cv2.dilate(erosion, kernel, iterations = 1)

cv2.imwrite("dilation.png", dilation)

