import numpy as np

def discounted_return(rewards, gamma):
  score =0.0
  for i in range(len(rewards)):
    score+=((gamma**i)* rewards[i])
  
  return score