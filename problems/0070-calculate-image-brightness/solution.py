
def calculate_brightness(img):
    if not img:
        return -1
    n=0
    col =len(img[0])
    if col ==0:
        return -1
    total =0
    for i in img:
        if len(i)!=col:
            return -1
        for j in i:
            if j < 0 or j > 255:
                return -1
            total+=j
            n+=1
    
    return round(total/n,2)