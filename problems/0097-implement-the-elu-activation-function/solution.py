import numpy as np
def elu(x: float, alpha: float = 1.0) -> float:
    val = 0
    if (x>0):
        val=x
    else:
        val=alpha * (np.exp(x)-1)
    return round(val,4)
    #  return np.where(x > 0, x, alpha * (np.exp(x) - 1))