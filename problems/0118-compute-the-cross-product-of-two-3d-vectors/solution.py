import numpy as np

def cross_product(a, b):
    final =[]
    
    first_comp = a[1]*b[2]-a[2]*b[1]
    second_comp = a[0]*b[2] - b[0]*a[2]
    third_comp = a[0]*b[1]-b[0]*a[1]

    final.append(first_comp)
    final.append(-second_comp)
    final.append(third_comp)
    return final