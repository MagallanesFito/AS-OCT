#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ESTE ES EL BUENO
import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_result(original,modified,title_original,title_modified):
	plt.subplot(121),plt.imshow(original),plt.title(title_original)
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(modified),plt.title(title_modified)
	plt.xticks([]), plt.yticks([])
	plt.show()
original_img = cv2.imread('6. AS-OCT/im1.jpeg',0)
#reducir su tamaño por la mitad.
img = cv2.resize(original_img, (0,0), fx=0.5, fy=0.5) 
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

''' Mantener un elemento estructurante lo suficientemente largo para quitar el ruido
en forma de barras verticales, pero no tanto como para omitir los limites de las corneas''' 
kernel = np.ones((1,6))

#dilation = cv2.dilate(thresh2,kernel,iterations = 1)
#kernel = np.ones((1,10))

erosion = cv2.erode(img,kernel,iterations = 1)
#kernel = np.ones((2,1))
#erosion2 = cv2.erode(erosion,kernel,iterations = 1)
#erosion = cv2.erode(thresh,kernel,iterations = 1)

edges_125 = cv2.Canny(erosion,125,200)
edges_150 = cv2.Canny(erosion,150,200)
#edges2 = cv2.Canny(erosion2,100,200)

cv2.imshow('Original',img)
''' 
Para este caso es mejor erosion horizontal solamente porue no importa el ruido 
que haya en la cornea, lo que me importa es la limitacion del borde. 
'''
cv2.imshow('Canny 125',edges_125)
cv2.imshow('Canny 150',edges_150)

cv2.waitKey(0)
cv2.destroyAllWindows()
