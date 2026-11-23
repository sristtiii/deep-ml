import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    term_one = 1/ len(X)
    secondterm =np.sum((y_true - (X@w))**2)
    thrid_term =  alpha * np.sum(w**2)
    return term_one*secondterm +thrid_term