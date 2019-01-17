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
'''def getBins(img):
	limits = 2
	average_coordinates = []
	n,m = img.shape
	for i in range(m):
		row_coordinates = []
		mask = False
		for j in range(n):
			if j-limits>=0 and j+limits<n:
				for k in range(-limits,limits+1):
					if img[j+k,i] == 255:
						mask = True
					else:
						mask = False
			if mask:


		average_coordinates.append(int(np.mean(row_coordinates)))
	return average_coordinates
'''
def getSignal(img):
	n,m = img.shape
	hist = np.zeros(n)
	for j in range(n):
		if img[j,0] == 255:
			hist[j] = 255
	return hist

original_img = cv2.imread('6. AS-OCT/im1.jpeg',0)

#reducir su tamaño por la mitad.
img = cv2.resize(original_img, (0,0), fx=0.5, fy=0.5) 

#filtrado
#blur = cv2.GaussianBlur(img,(5,5),1)
#blur = cv2.medianBlur(img,5)
#blur = cv2.bilateralFilter(img,9,75,75)
#cv2.imshow('blured',blur)
#thresholding
#ret,thresh1 = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)

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
kernel = np.ones((1,5))
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
#cv2.imshow('thres+erosion',opening)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#print(img.shape)
