import math 
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	final= {}
	
	final['sigmoid'] = (1/(1+math.exp(-x))) * (1-(1/(1+math.exp(-x)))) 
	final['tanh'] = 1- ((math.tanh(x))**2)
	value = max(0,x)
	if value >0 :
		final["relu"] = 1
	else :
		final['relu']=0
	return final