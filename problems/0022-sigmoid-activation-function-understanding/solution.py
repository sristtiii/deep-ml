import math

def sigmoid(z: float) -> float:
	den = 1+math.exp(-z)
	return 1/den