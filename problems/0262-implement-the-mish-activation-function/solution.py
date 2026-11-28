import math

def mish(x: float) -> float:
    return x*math.tanh(math.log(1+math.exp(x)))