def conditional_probability(data, x, y):
    count_x =0
    count_xy =0
    for i in range(len(data)):
      if(data[i][0]==x):
        count_x+=1
        if(data[i][1]==y):
          count_xy+=1
    if count_x ==0:
      return 0.0  
    return count_xy/count_x