"""
import numpy as np
import cv2

# Create a black image
img = np.zeros([512,512,1],dtype=np.uint8)

img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imwrite('test.png',img)
"""

import cv2
import numpy as np
img = np.zeros([512,512,1],dtype=np.uint8)
img.fill(255)
X=[0,100,5,0]
Y=[0,100,5,5]
cv2.line(img,(X[0],Y[0]),(X[1],Y[1]),(0,0,0),5)
cv2.imshow('Single Channel Window', img)

print("image shape: ", img.shape)
 
cv2.waitKey(0)
cv2.destroyAllWindows()