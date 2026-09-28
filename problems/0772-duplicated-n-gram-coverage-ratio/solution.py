def dup_ngram_ratio(text: str, n: int) -> float:
    tokens = text.split()
    if (len(tokens)<n):
        return 0.0
    listoftuple=[
        tuple(tokens[i:i+n])
        for i in range(len(tokens)-n+1)
    ]
    dit ={}
    for i in listoftuple:
        if i in dit:
            dit[i]+=1
        else:
            dit[i]=1

    duplicate =0
    for key,value in dit.items():
        if value >1:
            duplicate+=value

    valuee = duplicate/(len(listoftuple))
    return round(valuee,4)