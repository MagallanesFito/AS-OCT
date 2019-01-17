#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ESTE ES EL BUENO
import cv2
import matplotlib.pyplot as plt
import numpy as np

original_img = cv2.imread('6. AS-OCT/im8.jpeg',0)
#reducir su tamaño por la mitad.
img = cv2.resize(original_img, (0,0), fx=0.5, fy=0.5)
img2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
img2[:,:,0] = img
img2[:,:,1] = img
img2[:,:,2] = img
print(img.shape)
cv2.line(img2,(0,0),(50,50),(255,0,0),1)
cv2.imshow("imagen",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()