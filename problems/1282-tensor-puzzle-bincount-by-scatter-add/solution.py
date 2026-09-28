import numpy as np

def bincount(a: np.ndarray, n_bins: int) -> np.ndarray:
    bins =np.arange(n_bins)
    a =a[:,None]
    matches = (a ==bins)
    summ = np.sum(matches, axis=0) 
    return summ