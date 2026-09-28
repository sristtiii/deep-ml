import re

def tokenize(vocab, text, mode):
    if mode  =='encode':
        tokens = re.split(r'([,.:;?_!"()\']|--|\s)',text)
        unk= vocab['<|unk|>']
        indeee = [i.strip() for i in tokens if i.strip()]
        return [vocab.get(i,unk) for i in indeee]
    else:
        reverse_vocab = {}
        for key,value in vocab.items():
            reverse_vocab[value]=key
        # can be written as 
        # revers ={id : token for token,id in vocab.items()}
        tokens = [reverse_vocab[i] for i in text]
        # or could do 
        # toke =[]
        # for i in text:token.append(resver[i])
        result =""
        for i in tokens:
            if i in ',.?!":;()\'':
                result+=i
            else:
                result+=' '+i
        return result

    