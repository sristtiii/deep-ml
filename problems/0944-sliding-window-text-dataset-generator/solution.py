def sliding_window_dataset(token_ids: list[int], max_length: int, stride: int) -> list:
    if len(token_ids)<max_length+1:
        return []
    final =[]
    i=0
    while i+max_length<len(token_ids):
        inputt=(token_ids[i:i+max_length])
        outputt=(token_ids[i+1:i+max_length+1])
        final.append((inputt,outputt))
        i+=stride
    return final