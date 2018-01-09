import cv2
import numpy as np 


def result(image_location):
	'''
	Write the required function along with the required dependencies
	instead of

	image = cv2.imread(image_location)
	return image.shape
	
	'''
	image = cv2.imread(image_location)
	return image.shape