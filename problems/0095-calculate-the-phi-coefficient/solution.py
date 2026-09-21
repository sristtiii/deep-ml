import numpy as np
def phi_corr(x: list[int], y: list[int]) -> float:
	
	mean_x=0
	mean_y=0
	for i in x:
		mean_x+=i
	for j in y:
		mean_y+=j
	
	mean_x= mean_x/len(x)
	mean_y= mean_y/len(y)

	# print(mean_x,mean_y)

	var =0
	for (i,j) in zip(x,y):
		var+= (i-mean_x)*(j-mean_y)
	
	varx = 0
	for i in x:
		varx+=((i-mean_x)**2)

	vary =0
	for j in y:
		vary+=((j-mean_y)**2)

	if varx ==0 or vary == 0 or var==0:
		return 0.0

	phi = var /(np.sqrt(varx*vary))

	return np.round(phi, 4)