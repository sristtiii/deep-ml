def min_fill_time(grid):
    queue=[]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                queue.append((i,j))
            
    index =0
    count =0

    direc =[
        (0,1),(0,-1),(1,0),(-1,0)
    ]

    while index<len(queue):
        levels = len(queue) - index
        for _ in range(levels):
            r,c = queue[index]
            index+=1
            for dr,dc in direc:
                nc =dc+c
                nr =dr+r
                if 0<=nc<len(grid[0]) and 0<=nr<len(grid):
                    if grid[nr][nc] ==0:
                        grid[nr][nc] =1
                        queue.append((nr,nc))
        count+=1

    for r in grid :
        if 0 in r:
            return -1
    
    return count -1 if count >0 else 0
                    
