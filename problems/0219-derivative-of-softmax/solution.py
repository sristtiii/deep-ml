import math
def softmax_derivative(x: list[float]) -> list[list[float]]:
	
	total =0
	for i in x:
		total+=math.exp(i)
	
	# print(total)
	softmax_arr =[]
	for i in range(len(x)):
		softmax_arr.append((math.exp(x[i]))/total)
	# print(softmax_arr)

	# if u have to fgure out the sigmod and the jacobian matrix
	# so if same i and j its s*(1-s) and if (i!=j) -si sj

	jacobian = [[0.0 for _ in range(len(x))] for _ in range(len(x))]

	for i in range(len(x)):
		for j in range(len(x)):
			if(i==j):
				jacobian[i][j] =  softmax_arr[i] *(1-softmax_arr[i])
			else:
				jacobian[i][j] = -softmax_arr[i]* softmax_arr[j]
	return jacobian