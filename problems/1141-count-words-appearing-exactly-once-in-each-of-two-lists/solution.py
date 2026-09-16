def count_common_unique(list1, list2):
    dic ={}
    for i in list1:
        dic[i]= dic.get(i,0)+1
    dic2={}
    for j in list2:
        dic2[j]=dic2.get(j,0)+1

    count =0 
    for k,v in dic.items():
        if v ==1 and dic2.get(k,0) ==1:
            count+=1

    return count 