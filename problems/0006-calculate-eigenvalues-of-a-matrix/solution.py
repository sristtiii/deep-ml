import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace =0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(i==j):
				trace+=matrix[i][j]
	
	determinant =(matrix[0][0]* matrix[1][1] - matrix[0][1]* matrix[1][0])

	#HOW TO FIND THE SUM AND PRODUCt
	# new : you have to find the discriminant
	#-b+-sqrt (b**2 - 4ac/)2a
	#a=1,b=trace and c= determinan
	
	discriminant_formula = math.sqrt(trace**2 -( 4*determinant))
	lambda1 = (trace -discriminant_formula )/2
	lambda2 = (trace +discriminant_formula)/2
	listt=[lambda1,lambda2]
	#print(f"trace :-->{trace}, determinnat -->{determinant},diss-->{discriminant_formula}")
	listt.sort(reverse=True)
	return listt


