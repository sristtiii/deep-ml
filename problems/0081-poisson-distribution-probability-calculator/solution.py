import math

def poisson_probability(k, lam):
	e_val = math.exp(-lam)
	lam_val = lam**k

	total=1
	for i in range(1,k+1):
		total*=i

	return round((e_val*lam_val)/total, 4)