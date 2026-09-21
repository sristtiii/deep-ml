import numpy as np
import math
def descriptive_statistics(data: list | np.ndarray) -> dict:
    n = len(data)
    dic ={}
    mean =0
    data = sorted(data)
    for i in data:
        mean+=i
    dic["mean"] = mean/n

    if n%2!=0:
        dic["median"] = data[n//2]
    else:
        dic["median"] =  (data[(n-1)//2] + data[n//2])/2
    
    hashmap={}
    for i in data:
        if i in hashmap:
            hashmap[i] +=1
        else:
            hashmap[i]=1
    
    maxx= 0 
    mode = None
    for key,value in hashmap.items():
        if(value>maxx):
            maxx = value
            mode =key
    
    dic["mode"]= mode

    variance =0
    for i in data:
        variance += ((i-dic["mean"])**2)
    
    dic["variance"]=variance/n
    dic["standard_deviation"]=math.sqrt(variance/n)

    # percent_25 = (n-1)/4
    # percent_50 = (n-1)/2
    # percent_75 = (3*(n-1))/4

    dic["25th_percentile"]= np.percentile(data,25)
    dic["50th_percentile"]= np.percentile(data,50)
    dic["75th_percentile"]= np.percentile(data,75)

    iqr = dic["75th_percentile"]- dic["25th_percentile"]

    dic["interquartile_range"]= iqr
    return dic

















