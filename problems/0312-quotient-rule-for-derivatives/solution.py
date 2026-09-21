import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    gx = 0
    power_g = len(g_coeffs) - 1
    for i in range(len(g_coeffs)):
        gx += g_coeffs[i] * (x ** power_g)
        power_g -= 1

    hx = 0
    power_h = len(h_coeffs) - 1
    for i in range(len(h_coeffs)):
        hx += h_coeffs[i] * (x ** power_h)
        power_h -= 1

    # Reset powers here
    power_g = len(g_coeffs) - 1
    g_of_x = 0
    for i in range(len(g_coeffs) - 1):
        g_of_x += g_coeffs[i] * power_g * (x ** (power_g - 1))
        power_g -= 1

    power_h = len(h_coeffs) - 1
    h_of_x = 0
    for i in range(len(h_coeffs) - 1):
        h_of_x += h_coeffs[i] * power_h * (x ** (power_h - 1))
        power_h -= 1

    first_part = g_of_x * hx
    second_part = gx * h_of_x
    numerator = first_part - second_part
    denominator = hx ** 2

    total_term = numerator / denominator
    return total_term