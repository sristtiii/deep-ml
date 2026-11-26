import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    first = np.maximum(0,w1@x)
    second = np.maximum(0,w2@first)
    return np.maximum(0,second+x)
    