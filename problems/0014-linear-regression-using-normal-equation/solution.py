import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# usually linear regression formula y=wx+b the weights and the biasbut whn it comes to codeing the formula can be achieved by theta =(XtX)-1 xTy

	#transpose of the matrix
	transpose =[]
	for i in range(len(X[0])):
		listt=[]
		for j in range(len(X)):
			listt.append(X[j][i])
		transpose.append(listt)
	#print(transpose)
	
	first_matrix =[]
	for i in range(len(transpose)):
		listt=[]
		for j in range(len(X[0])):
			total=0
			for k in range(len(X)):
				total+=(transpose[i][k]*X[k][j])
			listt.append(total)
		first_matrix.append(listt)

	#i have to learn how to do the inverse of th marix manually,ik its like 1/deterX(agjacent X)
	xx =np.array(first_matrix)
	#remeber if the det ==0 then inverse is not possible 
	if(np.linalg.det(xx)==0):
		return []
	inverse = np.linalg.inv(xx)
	
	#by thi the first term is correct
	#we move to the next component Xt y

	sencond_matrix =[]
	for i in range(len(transpose)):
		total=0
		for k in range(len(y))	:
			total +=(transpose[i][k]* y[k])
		sencond_matrix.append(total)
	
	# now we multiply frst nad second 

	final_matrix =[]
	for i in range(len(inverse)):
		total=0
		for k in range(len(sencond_matrix)):
			total+=(inverse[i][k]*sencond_matrix[k])
		final_matrix.append(total)

	return final_matrix

