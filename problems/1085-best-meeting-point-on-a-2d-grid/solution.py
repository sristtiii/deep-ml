def best_meeting_point(grid):
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])

    row_list=[]
    col_list=[]
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                row_list.append(i)
                col_list.append(j)
    if not row_list:
        return 0

    row_list = sorted(row_list)
    col_list = sorted(col_list)  

    rm = row_list[len(row_list)//2]
    cm = col_list[len(col_list)//2]

    total =0
    for i in row_list:
        total+=abs(i-rm)

    for j in col_list:
        total+=abs(j-cm)
    return total    # if rm % 2 == 0:
    #     median_row =(row_list[rm-1] + row_list[rm] )//2
    # else:
    #     median_row=row_list[rm]
    # if cm % 2 == 0:
    #     median_col =(col_list[cm-1] + col_list[cm] )//2
    # else:
    #     median_col=col_list[cm]