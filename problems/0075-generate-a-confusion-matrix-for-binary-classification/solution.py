import numpy as np
from collections import Counter

def confusion_matrix(data):
	tp=0 #11
	tn=0 #00
	fp=0 #01
	fn=0 #10
	for i in range(len(data)):
		if(data[i][0]==1 and data[i][1]==1):
			tp+=1
		elif(data[i][0]==0 and data[i][1]==0):
			tn+=1
		elif(data[i][0]==0 and data[i][1]==1):
			fp+=1
		else :
			fn+=1
	
	matrixx =np.zeros((2,2), dtype=int)
	matrixx[0][0]=tp
	matrixx[0][1]=fn
	matrixx[1][0]=fp
	matrixx[1][1]=tn
	return matrixx