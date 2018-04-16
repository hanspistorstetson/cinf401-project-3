import cv2
import sys
import numpy as np

image = cv2.imread(sys.argv[1])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1)

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;

# Filter by Area.
params.filterByArea = True
params.minArea = 10000
params.maxArea = 1000000

params.filterByInertia = False
params.filterByConvexity = False


# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)

erosion = cv2.bitwise_not(erosion)
houghs = erosion.copy()
ret, erosion = cv2.threshold(erosion,127,255,cv2.THRESH_BINARY)
cv2.imwrite("erosion.png", erosion)
keypoints = detector.detect(erosion)
print(keypoints)
im_keypoints = cv2.drawKeypoints(erosion, keypoints, np.array([]), (255, 20, 147), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img = cv2.cvtColor(erosion,cv2.COLOR_GRAY2RGB)
for x in range(0,len(keypoints)):
    img=cv2.circle(img, (np.int(keypoints[x].pt[0]),np.int(keypoints[x].pt[1])), radius=np.int(keypoints[x].size), color=(0, 0,255), thickness=-1)
cv2.imwrite("wut.png", img)
