import numpy as np

def contractive_penalty(W, b, X):
    total=0.0
    for x in X:
        J= encoder_jacobian(W,b,x)
        total+=np.sum(J**2)
    return float(total/len(X))

def encoder_jacobian(W, b, x):
    z = (W@x)+b
    h = 1/(1+np.exp(-z))
    derivative_h = h *(1-h)
    J = derivative_h[:,None]*W
    return J

def kl_sparsity(H, rho):
    rho_hat = np.mean(H,axis=0)
    term1= rho * (np.log(rho/ rho_hat))
    term2 = (1-rho)*np.log((1-rho)/(1-rho_hat))
    return float(np.sum(term1+term2))

def kl_sparsity_grad(H, rho):
    N = H.shape[0]
    rho_hat= np.mean(H,axis =0)
    grad = (1 / N) * (-rho / rho_hat + (1 - rho) / (1 - rho_hat))
    return np.broadcast_to(grad, H.shape).copy()