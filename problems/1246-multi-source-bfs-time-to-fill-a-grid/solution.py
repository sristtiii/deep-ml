def min_fill_time(grid):
    queue=[]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                queue.append((i,j))

    front =0
    time =0

    direecions = [
        (-1,0),(1,0),(0,1),(0,-1)
    ]

    while front <len(queue):
        level = len(queue)-front
        for _ in range(level):
            r,c = queue[front]
            front+=1
            for dr,dc in direecions:
                nr = dr+r
                nc =dc +c  
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                    if(grid[nr][nc]) == 0:
                        grid[nr][nc ]=1
                        queue.append((nr,nc))
        time+=1
        
    for row in grid :
        if 0 in row:
            return -1

    return time-1 if time > 0 else 0






















