import numpy as np
import math
def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    answer =0
    if norm_type == 'l1':
        for i in arr:
            answer += (np.abs(i))
    elif norm_type=='l2':
        for i in arr:
            answer+=(i**2)
        answer=np.sqrt(answer)
    else:
        flat=[]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                flat.append(arr[i][j])
        for i in flat:
            answer+=(i**2)
        answer =float(np.sqrt(answer))
    return answer