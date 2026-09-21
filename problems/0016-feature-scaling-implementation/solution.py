import numpy as np 
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	mean = np.mean(data,axis =0)
	stand = np.std(data,axis =0)

	standardize = (data - mean )/stand
	min_val = np.min(data,axis =0)
	max_val = np.max(data,axis =0)
	normalise =(data - min_val) /(max_val-min_val)

	return standardize,normalise