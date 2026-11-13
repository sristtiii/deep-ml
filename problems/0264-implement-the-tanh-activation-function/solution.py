import numpy as np

def tanh(x: float) -> float:
    epos= np.exp(x)
    eneg = np.exp(-x)
    return (epos-eneg)/(epos+eneg)