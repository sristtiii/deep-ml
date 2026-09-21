import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	if ((len(a)*len(a[0])) != new_shape[0]*new_shape[1]):
		return []

	reshaped_matrix=[]
	listt=[]
	for i in range(len(a)):
		for j in range(len(a[0])):
			listt.append(a[i][j])
	
	#print(listt)
	x=0
	while(i<=new_shape[0]):
		new_matrix=[]
		for j in range(new_shape[1]):
			new_matrix.append(listt[x])
			x+=1
		i+=1
		reshaped_matrix.append(new_matrix)
	
	return reshaped_matrix