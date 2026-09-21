import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	arr = np.array(vectors)
	covariance_matrix = np.cov(arr)
	return covariance_matrix.tolist()