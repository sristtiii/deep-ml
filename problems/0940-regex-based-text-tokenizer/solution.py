import re

def tokenize_text(text: str) -> list:
    result =[]
    current =''
    i =0
    while i<len(text):
        c = text[i]

        if(c == " " or c == '\t' or c=='\n'):
            if(current!=''):
                result.append(current)
                current =''
        elif(c =='-' and ((1+i)<len(text)) and text[i+1]=='-'):
            if(current!=''):
                result.append(current)
                result.append('--')
                current =''
            i+=1
        elif (c == ',' or c =='.' or c ==':' or c ==';' or c=='?' or c=='_' 
        or c =='!' or c=='"' or c=='(' or c==')' or c == "'"):
            if (current!=''):
                result.append(current)
                current=''
            result.append(c)
        else:
            current+=c
        
        i+=1
    if current !='':
        result.append(current)
    return result