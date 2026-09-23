import numpy as np

def compute_tf_idf(corpus, query):
    if not corpus:
        return []
    document_count = len(corpus)
    tf =[]

    for i in range(len(corpus)):
        query_list=[]
        if len(corpus[i]) ==0:
            query_list=[0 for k in query]
            tf.append(query_list)
            continue

        for k in query:
            total=0
            for j in range(len(corpus[i])):
                if corpus[i][j]==k:
                    total+=1
            query_list.append(total/len(corpus[i]))
        tf.append(query_list)


    idf=[]

    for k in query:
        df =0
        for i in range(len(corpus)):
            for j in range(len(corpus[i])):
                if corpus[i][j]==k:
                    df+=1
                    break

        value = np.log((document_count + 1) / (df + 1)) + 1
        idf.append(value)

    result=[]
    for i in range(len(corpus)):
        row =[]
        for j in range(len(query)):
            row.append(tf[i][j]*idf[j])
        result.append(row)
    return np.round(result,5).tolist()