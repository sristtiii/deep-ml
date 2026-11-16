import numpy as np
def orthogonal_projection(v, L):
    vv = np.asarray(v)
    ll = np.asarray(L)
    return ((vv@ll)/(ll@ll)*ll)