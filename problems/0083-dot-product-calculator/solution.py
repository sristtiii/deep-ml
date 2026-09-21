import numpy as np

def calculate_dot_product(vec1, vec2):
	#return np.dot(vec1,vec2)

	total =0
	for i in range(len(vec1)):
		for j in range(len(vec2)):
			if i==j:
				total+=(vec1[i]*vec2[j])
	return total