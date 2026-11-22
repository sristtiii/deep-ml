import numpy as np

def calculate_contrast(img) -> int:
    max_val =np.max(img)
    min_val =np.min(img)
    return max_val-min_val