def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    c=[]
    for i in range(len(a)):
        rows_within=[]
        for j in range(len(a[0])):
            total =0
            for k in range(len(b)):
                total+= a[i][k]* b[k][j]
            rows_within.append(total)
        c.append(rows_within)
    return c