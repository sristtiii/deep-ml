import numpy as np
import math
def log_softmax(scores: list) -> np.ndarray:
	max_val =max(scores)
	e_scores=[]
	total=0

	for i in range(len(scores)):
		x = math.exp(scores[i]-max_val)
		e_scores.append(x)
		total+=x
	
	final_result=[]
	for i in range(len(e_scores)):
		final_result.append(np.round(math.log(e_scores[i]/total), 4))
	
	return final_result