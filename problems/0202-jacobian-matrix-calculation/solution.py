import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	
	original = f(x)
	#print(original)

	xx = x.copy()
	xx[0]+=h
	deri_x = f(xx)

	#print(deri_x)

	dx =[]
	for i in range(len(original)):
		dx.append((deri_x[i] - original[i])/h)
	#print(dx)

	yy = x.copy()
	yy[1]+=h
	deri_y = f(yy)
	#print(deri_y)

	dy =[]
	for i in range(len(original)):
		dy.append((deri_y[i]-original[i])/h)
	##print(dy)

	if((len(x))==3):
		zz = x.copy()
		zz[2]+=h
		deri_z = f(zz)
		#print(deri_y)

		dz =[]
		for i in range(len(original)):
			dz.append((deri_z[i]-original[i])/h)
	
	jacobian=[]
	for i in range(len(original)):
		if (len(x))==2:
			jacobian.append([dx[i], dy[i]])
		elif (len(x))==3:
			jacobian.append([dx[i], dy[i],dz[i]])

	return jacobian