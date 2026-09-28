
import numpy as np

def rmse(y_true, y_pred):
	total = np.mean((y_pred-y_true)**2)
	rmse_res = np.sqrt(total)
	return round(rmse_res,3)
