def vocab_size(tokens, special_tokens=None):
    mm =set(tokens)
    if special_tokens is not None:
        mm.update(special_tokens)
    return len(mm)