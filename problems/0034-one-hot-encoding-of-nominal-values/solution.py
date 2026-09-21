import numpy as np

def to_categorical(x, n_col=None):
	n = len(x)
	
	encode = np.zeros((n,np.max(x)+1))

	for i in range(len(x)):
		encode[i][x[i]]=1
	return encode

		
	