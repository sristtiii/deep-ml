import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    i = np.arange(A.shape[0])
    return A[i,i]