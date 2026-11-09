import numpy as np

def compute_td_error(v_s: float, reward: float, v_s_prime: float, gamma: float, done: bool) -> float:
    target = reward + (gamma*v_s_prime )
    return target - v_s