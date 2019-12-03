import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
a=cv2.imread('sample.jpg', 1)
cv2.imshow('Hello',a)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Random Matrix to Generate a Random Image
d=np.random.randint(0,255,(1280,1280,3))
print(d)

#Save Random Image
cv2.imwrite('sample1.jpg',d)

#Display Random Image
cv2.imshow('',cv2.imread('sample1.jpg', 1))
k=cv2.waitKey()
if k== 27:
    cv2.destroyAllWindows()





