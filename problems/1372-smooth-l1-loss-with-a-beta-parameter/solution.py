import numpy as np

def smooth_l1(pred, target, beta=1.0, reduction='mean'):
    pred =np.asarray(pred)
    target = np.asarray(target)
    if beta <= 0:
        raise ValueError("beta must be greater than 0")
    if reduction not in ('none', 'mean', 'sum'):
        raise ValueError("Invalid reduction")
    x = pred - target
    last =[]
    #but idk what is with the reduction 
    for i in x.flat:
        if np.abs(i)<beta:
            value = (0.5*(i**2))/beta
        else:
            value =np.abs(i)- (0.5*beta)
        last.append(value)
    lastt =np.array(last).reshape(x.shape)

    if reduction == 'none':
        return lastt
    elif reduction =='mean':
        return float(np.mean(lastt))
    elif reduction == 'sum':
        return float(np.sum(lastt))
    else:
        return ValueError("Invalid reduction")