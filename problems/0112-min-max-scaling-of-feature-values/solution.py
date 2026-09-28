import numpy as np
def min_max(x: list[float]) -> list[float]:
    min_val = np.min(x, axis=None)
    max_val = np.max(x, axis=None)

    for i in range(len(x)):
        x[i] = (x[i]-min_val)/(max_val-min_val)
    
    return x