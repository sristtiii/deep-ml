import numpy as np

def explained_variance_ratio(X):
    mean = np.mean(X,axis =0)
    std = np.std(X,axis =0)
    standardize = (X-mean)
    cov = np.cov(standardize,rowvar=False)
    eigen_val , eigne_vec = np.linalg.eigh(cov)
    total_eigen_val = np.sum(eigen_val)
    eigen_val = eigen_val[::-1]
    ratio_mat = eigen_val/total_eigen_val
    return ratio_mat
