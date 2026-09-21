import math

def softmax(scores: list[float]) -> list[float]:
    e_scores =[]
    max_val = max(scores)
    total =0
    for i in range(len(scores)):
        x =math.exp(scores[i]-max_val)
        e_scores.append(x)
        total+=x
    
    result =[]
    for i in range(len(e_scores)):
        result.append(e_scores[i]/total)
    
    return result