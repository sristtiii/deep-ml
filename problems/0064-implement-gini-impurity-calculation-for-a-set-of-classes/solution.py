import numpy as np
def gini_impurity(y):
    zeros ,ones,two=0,0,0
    for i in range(len(y)):
        if y[i]==0:
            zeros+=1
        elif y[i]==1:
            ones+=1
        else:
            two+=1
    zeros=zeros/len(y)
    ones=ones/len(y)
    two = two/len(y)
    val = 1-((zeros**2)+ (ones**2)+(two**2))
    return round(val,3)