import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    col_a = a[:,None]
    return col_a * b