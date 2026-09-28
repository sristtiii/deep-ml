def build_vocab(tokens):
    if tokens == None:
        return {}

    sort = sorted(tokens)
    my_dic= {}
    a=0
    for i in sort:
        if i not in my_dic:
            my_dic[i] = a
            a+=1

    return my_dic