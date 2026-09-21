import numpy as np

def make_diagonal(x):
	
	zero_matrix =np.zeros((len(x),len(x)))

	for i in range(len(zero_matrix)):
		for j in range(len(zero_matrix[0])):
			if(i==j):
				zero_matrix[i][j]=x[i]
	
	return zero_matrix