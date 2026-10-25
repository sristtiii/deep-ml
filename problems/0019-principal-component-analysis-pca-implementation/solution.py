import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    mean =np.mean(data, axis=0)
    std =np.std(data,axis=0)
    standardize =(data -mean) /std
    cov = np.cov(standardize,rowvar=False)
    eigen_val,eigen_vec = np.linalg.eigh(cov)
    eigen_vec = eigen_vec[:, ::-1]
    pca = eigen_vec[:,:k].copy()

    for i in range(k):
        for j in range(pca.shape[0]):
            if abs(pca[j][i])>1e-10:
                if pca[j][i] <0:
                    pca[:,i]*=-1
                break
    return pca