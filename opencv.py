
import cv2
import sys
import numpy as np



params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;

# Filter by Area.
params.filterByArea = True
params.minArea = 2500

params.filterByInertia = False
params.filterByConvexity = False


# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)
name = "/bigdata/data/pan-starrs1/" + sys.argv[1]
sys.stderr.write(name + "\n")
image = cv2.imread(name)
if image.shape is None:
    exit(0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1)
erosion = cv2.bitwise_not(erosion)
ret, erosion = cv2.threshold(erosion,127,255,cv2.THRESH_BINARY)

keypoints = detector.detect(erosion)
im_keypoints = cv2.drawKeypoints(erosion, keypoints, np.array([]), (255, 20, 147), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img = cv2.cvtColor(erosion,cv2.COLOR_GRAY2RGB)

list_of_points = []
with open("/bigdata/data/pan-starrs1/radec.csv") as f:
    ra_image = 0.0
    dec_image = 0.0
    for line in f:
        line = line.strip()
        line = line.split(",")
        filename = (name.split(".png")[0].split("/")[-1])
        if (line[0] == filename): 
            ra_image = float(line[1])
            dec_image = float(line[2])
            break
    for x in range(len(keypoints)):
        ra = ra_image + (0.25/3600) * ((img.shape[1] - keypoints[x].pt[0]) - img.shape[1]/2) 
        dec = dec_image + (0.25/3600) * ((img.shape[0] - keypoints[x].pt[1]) - img.shape[0]/2)
        size = keypoints[x].size
        list_of_points.append((ra, dec, size))

for p in list_of_points:
    print(p)
