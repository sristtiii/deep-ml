def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[1][0]
    d=matrix[1][1]
    determinant =(a*d)-(b*c)

    if(determinant ==0):
        return None
    inv= [[d,-b],[-c,a]]
    matrix_inverse = 1/determinant

    for i in range(len(inv)):
        for j in range(len(inv[0])):
            inv[i][j] = matrix_inverse * inv[i][j]
    
    return inv
    

