import cv2
import numpy as np
import matplotlib.pyplot as plt

image_one = cv2.imread('kirs1.png', 0) 
image_two = cv2.imread('kirs2.png', 0)

def ShowDisparity(bSize=5):
    stereo = cv2.StereoBM_create(num_discrepancy=32, blockSize=bSize) 
    discrepancy = stereo.compute(image_one, image_two)
    min = discrepancy.min()
    max = discrepancy.max()
    discrepancy = np.uint8(255 * (discrepancy - min) / (max - min)) 
    return discrepancy


result = ShowDisparity(bSize=5) 
print(result) 
plt.imshow(result, 'gray') 
cv2.imwrite("output.png", result)
plt.axis('off')
plt.show()