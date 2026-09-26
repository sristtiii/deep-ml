import numpy as np

def ucb_action(counts, values, t, c):
  # ucb = qt+c* sqrt (in(t)/ n)
  bonus = c *np.sqrt((np.log(t))/counts)
  x = values+bonus
  return np.argmax(x)
  

