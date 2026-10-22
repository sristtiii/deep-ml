import numpy as np

def mds(D: np.ndarray, k: int) -> np.ndarray:

    DD =D**2
    n=D.shape[0]
    I=np.eye(n)
    J=np.ones((n,n))
    H= I-((1/n)*J)
    b =(-0.5)* H @ DD @ H
    eigen_vaues ,eigen_vector = np.linalg.eigh(b)
    idx = np.argsort(eigen_vaues)[::-1]
    eigen_vaues =eigen_vaues[idx][:k]
    eigen_vaues =  np.clip(eigen_vaues,0,None)
    eigen_vector=eigen_vector[:,idx][:,:k]
    for j in range(k):
        col = eigen_vector[:,j]
        nonzero = np.flatnonzero(np.abs(col)>1e-10)
        if len(nonzero)>0 and col[nonzero[0]]<0:
            eigen_vector[:,j]*=-1
    x = eigen_vector * np.sqrt(eigen_vaues)
    return x