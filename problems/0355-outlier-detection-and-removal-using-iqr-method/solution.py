import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:

	if not data:
		return {
		'cleaned_data': [],
		'outlier_indices': [],
		'lower_bound': None,
		'upper_bound': None
		} 

	sortedd = sorted(data)
	n= len(data)
	q1 = np.percentile(sortedd, 25)
	q3 = np.percentile(sortedd, 75)
	iqr = q3 - q1

	lower_bound = float(q1 - (k * iqr))
	upper_bound = float(q3 + (k * iqr))

	clean=[]
	outl=[]
	for i in range(n):
		if lower_bound<= data[i] <= upper_bound:
			clean.append(data[i])
		else:
			outl.append(i)
	
	return {
		'cleaned_data': clean,
		'outlier_indices': outl,
		'lower_bound': lower_bound,
		'upper_bound': upper_bound
		}