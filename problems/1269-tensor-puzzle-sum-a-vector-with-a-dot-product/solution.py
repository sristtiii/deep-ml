import numpy as np

def vector_sum(a: np.ndarray):
    sam = (np.arange(len(a))*0)+1.0
    return a@ sam