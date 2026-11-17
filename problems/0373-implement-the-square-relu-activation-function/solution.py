import numpy as np

def square_relu(x: np.ndarray) -> dict:
    
    x=np.asarray(x)
    output=np.where(x>0,x**2,0.0)
    dic =np.where(x>0,x*2,0.0)
    return {
        "output":output,
        "derivative":dic
    }