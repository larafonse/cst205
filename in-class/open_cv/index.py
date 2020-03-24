import numpy as np
import cv2

creed_gray = cv2.imread('images/creed.png', cv2.IMREAD_GRAYSCALE)
creed_remap = cv2.applyColorMap(creed_gray, cv2.COLORMAP_COOL)

cv2.imshow("creed boi", creed_remap)
cv2.waitKey()