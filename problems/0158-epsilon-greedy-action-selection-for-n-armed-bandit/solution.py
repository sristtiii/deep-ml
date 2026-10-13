import numpy as np

def epsilon_greedy(Q, epsilon=0.1):
    if np.random.random()<epsilon:
        return np.random.randint(len(Q))
    else:
        return np.argmax(Q)