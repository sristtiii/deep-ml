import numpy as np
import math
def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)² =x**2 -2xy+y**2
		point: Point (x, y) or (x, y, z) at which to evaluate
	"""
	final_tuple=()
	if(func_name == 'poly2d'):
		fd_dx = (2* point[0] *point[1]) +(point[1]**2)
		fd_dy = (point[0]**2) +(2* point[0] *point[1])
		return (fd_dx,fd_dy)
	elif(func_name == 'exp_sum'):
		fd_dx = math.exp(point[0] + point[1])
		fd_dy = math.exp(point[0] + point[1])
		return (fd_dx,fd_dy)
	elif(func_name == 'product_sin'):
		fd_dx = math.sin(point[1])
		fd_dy = point[0]* math.cos(point[1])
		return (fd_dx,fd_dy)
	elif(func_name == 'poly3d'):
		fd_dx = (2* point[0] *point[1])
		fd_dy = (point[0]**2) + (point[2]**2) 
		fd_dz = (2* point[1] *point[2])
		return (fd_dx,fd_dy,fd_dz)
	elif(func_name == 'squared_error'): #x**2 -2xy+y**2
		fd_dx = (2* point[0])- (2* point[1]) 
		fd_dy = (2* point[1])- (2* point[0]) 
		return (fd_dx,fd_dy)
	return final_tuple