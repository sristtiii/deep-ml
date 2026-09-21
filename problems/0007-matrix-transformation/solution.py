import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	#numpy whatis it ?
	#nd array,math cmputation of array

	#linalg = linear algebra builft in modules /paclages

	#invertible ot not 
	#if det ==0 then not , only !=0 thery are invertible 

	if (np.linalg.det(T) == 0 or np.linalg.det(S) ==0):
		return -1

	#mat multiplxcation in cummulative a(bc)= (ab)c

	AS = np.matmul(A,S)
	#usually T1 = 1/ det T (adj T)

	T_inverse = np.linalg.inv(T)

	final_matrix = np.matmul(T_inverse,AS)
	return final_matrix