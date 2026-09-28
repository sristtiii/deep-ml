
import numpy as np

def r_squared(y_true, y_pred):
	
	mean = np.mean((y_true -y_pred)**2)
	total=0
	for i in range(len(y_pred)):
		total+=(y_pred[i])
	
	total/=len(y_pred)
	avg =np.mean((y_true-total)**2)
	return 1-(mean/avg)

