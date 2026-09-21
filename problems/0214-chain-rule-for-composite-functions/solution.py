import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	derivative =1.0
	for i in reversed(functions):
		if (i=='square'):
			derivative *= (2*x)
			x = (x**2)
		elif(i == 'sin'):
			derivative *= (np.cos(x))
			x = np.sin(x)
		elif(i == 'log'):
			derivative *= (1/x)
			x = np.log(x)
		elif(i =='exp'):
			derivative *= (np.exp(x))
			x = np.exp(x)
		else:
			return 0.0
	return derivative




