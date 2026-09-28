import string

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    match_count =0
    if (len(predictions)==0 and len(references)==0):
        return 0.0

    for i in range(len (predictions)):
        pred_val = predictions[i];
        ref_val = references[i];

        pred_val = pred_val.lower()
        ref_val = ref_val.lower()

        for i in string.punctuation:
            pred_val = pred_val.replace(i,"")
            ref_val = ref_val.replace(i,"")

        pred_val = " ".join(pred_val.split())
        ref_val = " ".join(ref_val.split())
        
        if pred_val== ref_val:
            match_count+=1
        
    return match_count/len(predictions)