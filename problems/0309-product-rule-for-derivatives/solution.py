import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    
    all_terms= [0  for _ in range(len(f_coeffs)+len(g_coeffs)-1)]

    for i in range(len(f_coeffs)):
        for j in range(len(g_coeffs)):
            index =i+j
            all_terms[index]+=(f_coeffs[i]*(g_coeffs[j]))

    final=[]    
    for i in range(1,len(all_terms)):
        final.append(i*all_terms[i])
    if not final:
        return [0.0]
    return final

