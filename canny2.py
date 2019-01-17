#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

#morphological operatars
kernel = np.ones((1,6))
#dilation = cv2.dilate(thresh2,kernel,iterations = 1)
#kernel = np.ones((1,10))
erosion_h = cv2.erode(img,kernel,iterations = 1)



#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#kernel = np.ones((2,1))
#erosion2 = cv2.erode(erosion,kernel,iterations = 1)
#erosion = cv2.erode(thresh,kernel,iterations = 1)

edges_h = cv2.Canny(erosion_h,100,200)

kernel = np.ones((20,20))
edges_opening = cv2.morphologyEx(edges_h, cv2.MORPH_OPEN, kernel)
edges_closing = cv2.morphologyEx(edges_h, cv2.MORPH_CLOSE, kernel)
#edges_closing = cv2.Canny(closing,100,200)
#edges_gradient = cv2.Canny(gradient,100,200)
#edges_tophat = cv2.Canny(tophat,100,200)
#edges_blackhat = cv2.Canny(blackhat,100,200)
#edges2 = cv2.Canny(erosion2,100,200)

cv2.imshow('Original',img)
''' 
Para este caso es mejor erosion horizontal solamente porue no importa el ruido 
que haya en la cornea, lo que me importa es la limitacion del borde. 
'''
cv2.imshow('Canny h ',edges_closing)




cv2.waitKey(0)
cv2.destroyAllWindows()

#edges = cv2.Canny(thresh1,100,200)
#quitar ruido de la imagen


#morphological operatars
'''kernel = np.ones((3,1))
dilation = cv2.dilate(thresh2,kernel,iterations = 1)
kernel = np.ones((1,10))
erosion1 = cv2.erode(dilation,kernel,iterations = 1)
'''
#blur = cv2.medianBlur(img,10)
#blur = cv2.bilateralFilter(img,9,75,75)
'''kernel = np.ones((1,5))
opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
#erosion1 = cv2.erode(thresh2,kernel,iterations = 1)
#erosion2 = cv2.erode(thresh1,kernel,iterations = 2)
#cv2.imshow('gaussian + thresh',thresh1)
#cv2.imshow('gaussian + thresh+canny',edges)
#cv2.imshow('gaussian + thresh+erosion1',erosion1)
#cv2.imshow('gaussian + thresh+erosion2',img)
#cv2.imshow('thres+erosion',thresh2)

bins = [i for i in range(s)]
histogram = getSignal(opening)
plt.hist(histogram,)
plt.show()
#print(opening[140,19])


#print(img.shape)
'''