def score_dialog_complexity(dialogs):
    final =[]

    for i in range(len(dialogs)):
        myset=set()
        for j in range(len(dialogs[i])):
            myset.add(dialogs[i][j])
        new_tuple=(i,len(myset))
        final.append(new_tuple)
    
    return sorted(final,key=lambda x: (-x[1],x[0]))
