def exp_weighted_average(Q1, rewards, alpha):
    total = 0
    n = len(rewards)
    for i in range(n):
        total+= alpha*((1-alpha)**(n-1-i)*rewards[i])
    return ((1-alpha)**n)* Q1+ total