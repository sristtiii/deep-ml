import numpy as np

def calculate_perplexity(probabilities: list[float]) -> float:
    total =0
    for i in probabilities:
        total+= np.log(i)
    
    aver = total/len(probabilities)
    exp = np.exp(-aver)
    return exp