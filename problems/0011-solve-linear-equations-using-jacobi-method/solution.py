import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    # Initialize x with zeros
    x = np.zeros(len(b), dtype=float)

    # Perform exactly n iterations
    for _ in range(n):
        x_new = np.zeros_like(x)
        for i in range(len(b)):
            s = 0.0
            for j in range(len(b)):
                if i != j:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new

    # Round only the final result
    return [round(val, 4) for val in x]