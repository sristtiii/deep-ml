import numpy as np

def smooth_bigram_probs(N, k):
    count_num =0
    for i in range(len(N)):
        for j in range(len(N[i])):
            N[i][j]+=k
    total_count =[]
    for i in range(len(N)):
        count =0
        for j in range(len(N[i])):
            count+=N[i][j]
        total_count.append(count)


    result =[]
    for i in range(len(N)):
        matrix =[]
        for j in range(len(N[i])):
            count_num = N[i][j]
            matrix.append(count_num/total_count[i])
        result.append(matrix)

    return result 