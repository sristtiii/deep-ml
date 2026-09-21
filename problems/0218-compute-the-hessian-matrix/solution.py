from typing import Callable
import numpy as np
def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
# remeeber jacobian id f(x+h)-f(x)/h
# where as the hessian will be nxn matrix 
# i==j value = f(x+h)-2f(x)+f(x-h)/h^2
# if i!=j f(++)-f(+-)-f(-+)+f(--)/4h^2
	n = len(point)
	original =f(point)
	hessian = np.zeros((n,n))

	for i in range(n):
		for j in range(n):
			if i == j:
				plus_value = point.copy()
				min_value = point.copy()

				plus_value[i]+=h
				min_value[i]-=h

				final_value = ((f(plus_value)-(2*original)+f(min_value))/h**2)
				hessian[i][j]=final_value
			else :
				plus_plus=point.copy()
				minus_minus=point.copy()
				plus_minus=point.copy()
				minus_plus=point.copy()

				plus_plus[i]+=h
				plus_plus[j]+=h

				minus_minus[i]-=h
				minus_minus[j]-=h

				plus_minus[i]+=h
				plus_minus[j]-=h

				minus_plus[i]-=h
				minus_plus[j]+=h

				final_value = (f(plus_plus)-f(plus_minus)-f(minus_plus)+f(minus_minus))/(4*(h**2))
				hessian[i][j]=final_value 
	return hessian.tolist()