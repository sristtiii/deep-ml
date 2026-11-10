import numpy as np

def kl_divergence_estimator(pi_theta: np.ndarray, pi_ref: np.ndarray) -> np.ndarray:
    return (pi_ref/pi_theta)- np.log(pi_ref/pi_theta)-1