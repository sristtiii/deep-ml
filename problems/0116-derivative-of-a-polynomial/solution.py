def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    first = c* n 
    second =n-1
    third = first*x**second
    return third
    pass