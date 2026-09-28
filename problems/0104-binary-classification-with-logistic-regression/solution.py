import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:

	z = 0
	total_z=[]
	for i in range(len(X)):
		for j in range(len(X[0])):
			z += (X[i][j]* weights[j])#z = wx+b
		z+=bias
		z =1/(1+np.exp(-z))
		if z>=0.5: 
			z=1
		else:
			z=0
		total_z.append(z)
	return total_z
	
