import numpy as np

def pca_reconstruction_error(X: np.ndarray, n_components: int) -> float:
    mean =np.mean(X,axis=0)
    standarise = X- mean
    cov = np.cov(standarise,rowvar=False, bias=True)
    #this is population covariance hences its bias true
    #or u can standardse.T @standardize /n
    eigen_values,eigen_Vectors = np.linalg.eigh(cov)
    eigen_values = eigen_values[::-1][:n_components]
    eigen_Vectors = eigen_Vectors[:,::-1][:,:n_components]
    Z = standarise @ eigen_Vectors
    #reconstruct the original data so
    x_reconstruct =  Z @ eigen_Vectors.T
    x_reconstruct = x_reconstruct +mean
    error = np.mean((X-x_reconstruct)**2)
    return error