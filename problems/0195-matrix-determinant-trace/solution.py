import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	finall =set()
	trace=0
	dte=np.linalg.det(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i==j:
				trace+=matrix[i][j]
			
	
	finall.add(dte)
	finall.add(trace)
	return finall		