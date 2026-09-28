def most_frequent_pair(sequences):
    my_dictv ={}

    for sequence in sequences:
        for i in range(len(sequence)-1):
            x=(sequence[i],sequence[i+1])
            my_dictv[x] = my_dictv.get(x,0)+1
    
    if not my_dictv:
        return None
    maxx = max(my_dictv.values())

    for key,value in my_dictv.items():
        if value==maxx:
            return key
    
    return None