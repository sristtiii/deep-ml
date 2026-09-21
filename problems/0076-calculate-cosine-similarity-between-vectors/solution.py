import numpy as np
import math 

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# cosine sialryt =adot b/ mag a * mag b

	total =0
	for i in range(len(v1)):
		for j in range(len(v2)):
			if(i==j):
				total+=(v1[i]*v2[j])
	
	mag=0
	for i in range(len(v1)):
		mag+= (v1[i]**2)

	magnitude_A = math.sqrt(mag)

	mgg =0
	for i in range(len(v2)):
		mgg+=(v2[i]**2)
	magnitude_B = math.sqrt(mgg)

	finalvalue =(total)/ (magnitude_A*magnitude_B)
	return finalvalue