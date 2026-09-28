import numpy as np

def discounted_return(rewards, gamma):
    rewards= np.asarray(rewards)
    discount= gamma** np.arange(len(rewards))
    return np.sum(rewards*discount)
# def discounted_return(rewards, gamma):
#     final_g =0
#     for i in range(len(rewards)):
#         final_g+=(gamma**i)*rewards[i]
#     return final_g