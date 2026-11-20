import numpy as np
def swish(x: float) -> float:
    return x* (1/(1+np.exp(-x)))