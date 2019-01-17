#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ESTE ES EL BUENO
import cv2
import matplotlib.pyplot as plt
import numpy as np

def drawLines(img,img_edges):
	columnas = {}
	n,m = img_edges.shape
	for i in range(m):
		bordes = []
		for j in range(n):
			if(len(bordes)) == 5:
				columnas[i] = bordes
				break
			if(img_edges[j,i] == 255):
				if(len(bordes) < 4):
					if(img_edges[j-1,i] == 0 and img_edges[j+1,i] == 0):
						bordes.append(j)
				else:
					bordes.append(j)
	##Continuar algoritmo
	deleted = []
	for key,value in columnas.items():
		if((value[1]-value[0])>5 or (value[3]-value[2])>4 or (value[4]-value[0])>135):
			deleted.append(key)
	for e in deleted:
		del columnas[e]
	#Identificar outliers
	deleted = []
	value_0 = []
	value_1 = []
	value_2 = []
	value_3 = []
	value_4 = []

	for key,value in columnas.items():
		value_0.append(value[0])
		value_1.append(value[1])
		value_2.append(value[2])
		value_3.append(value[3])
		value_4.append(value[4])

	v0_stats = (np.mean(value_0),np.std(value_0))
	v1_stats = (np.mean(value_1),np.std(value_1))
	v2_stats = (np.mean(value_2),np.std(value_2))
	v3_stats = (np.mean(value_3),np.std(value_3))
	v4_stats = (np.mean(value_4),np.std(value_4))
	#3 desviaciones estandar 
	threshold = 3

	for key,value in columnas.items():
		#value 0
		z_score = (value[0]-v0_stats[0])/v0_stats[1]
		if(abs(z_score)>threshold):
			if key not in deleted:
				deleted.append(key)
		#value 1
		z_score = (value[1]-v1_stats[0])/v1_stats[1]
		if(abs(z_score)>threshold):
			if key not in deleted:
				deleted.append(key)
		#value 2
		z_score = (value[2]-v2_stats[0])/v2_stats[1]
		if(abs(z_score)>threshold):
			if key not in deleted:
				deleted.append(key)
		#value 3
		z_score = (value[3]-v3_stats[0])/v3_stats[1]
		if(abs(z_score)>threshold):
			if key not in deleted:
				deleted.append(key)
		#value 4
		z_score = (value[4]-v4_stats[0])/v4_stats[1]
		if(abs(z_score)>threshold):
			if key not in deleted:
				deleted.append(key)
	for e in deleted:
		del columnas[e]

	#Calcular medidas
	va = [(value_0[i]+value_1[i])/2 for i in range(len(value_0))]
	vc = [(value_2[i]+value_3[i])/2 for i in range(len(value_2))]

	LC = np.mean([(value_4[i]-va[i]) for i in range(len(value_4))])
	LP = np.mean([(vc[i]-va[i]) for i in range(len(va))])

	#Obtner por promedio#

	i = 0
	max_ = 0
	key_ = 0
	#Encuentra la diferencia mas grande y muesrta esa medida
	for key,value in columnas.items():
		if(i == 0):
			max_ = value[4]-value[0]
			key_ = key
		else:
			if(value[4]-value[0]>max_):
				max_ = value[4] - value[0]
				key_ = key
		i = i+1
	final_img = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
	final_img[:,:,0] = img
	final_img[:,:,1] = img
	final_img[:,:,2] = img
	print("MAYOR DIFERENCIA: (Azul)")
	lc = (columnas[key_][4] - columnas[key_][0])
	print("Lente Cornea: ")
	print(lc)
	print("Lente")
	lp = (columnas[key_][2] - columnas[key_][0])
	print(lp)
	print("Ratio: ")
	radio = lp/lc
	print(radio)
	cv2.line(final_img,(key_,columnas[key_][0]),(key_,columnas[key_][4]),(255,0,0),2)

	print("----------------------------------")
	print("PROMEDIO: ")
	print("Lente-cornea:")
	print(LC)
	print("Lente: ")
	print(LP)
	print("Ratio: ")
	ratio = LP/LC
	print(ratio)

	return final_img



original_img = cv2.imread('6. AS-OCT/im12.jpeg',0)
#reducir su tamaño por la mitad.
img = cv2.resize(original_img, (0,0), fx=0.5, fy=0.5) 

''' Mantener un elemento estructurante lo suficientemente largo para quitar el ruido
en forma de barras verticales, pero no tanto como para omitir los limites de las corneas''' 
kernel = np.ones((1,6))

erosion = cv2.erode(img,kernel,iterations = 1)
erosion_4 = cv2.erode(img,kernel,iterations = 4)
edges_100 = cv2.Canny(erosion_4,100,200)
edges_125 = cv2.Canny(erosion,125,200)
edges_150 = cv2.Canny(erosion,150,200)
cv2.imshow('Original',img)
''' 
Para este caso es mejor erosion horizontal solamente porue no importa el ruido 
que haya en la cornea, lo que me importa es la limitacion del borde. 
'''
#cv2.imshow('Canny 125',edges_125)
cv2.imshow('Canny 150',edges_150)

final_img = drawLines(img,edges_150)
cv2.imshow("Final",final_img)

#print(edges_125[120,217])
#print(edges_125[123,217])


cv2.waitKey(0)
cv2.destroyAllWindows()

#217,120
#217,123