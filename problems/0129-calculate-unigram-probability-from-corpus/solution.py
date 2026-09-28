def unigram_probability(corpus: str, word: str) -> float:
    result = corpus.split()
    
    ss =set()
    total=0
    for i in result:
        if(i==word):
            total+=1
    return total/len(result)