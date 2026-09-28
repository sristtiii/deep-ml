import re

def encode(text, vocab):
    n = len(text)
    asplits = re.split(r'([,.:;?_!"()\']|--|\s)',text)
    final = [x for x in asplits if x.strip()]
    fz = [vocab[a] for a in final if a in vocab]
    return fz
def decode(ids, vocab):
    inver = {v:k for k,v in vocab.items()}
    toek =[inver[i] for i in ids]
    text = " ".join(toek)
    textt = re.sub(r'\s+([,.?!"()\'])',r"\1",text)
    return textt