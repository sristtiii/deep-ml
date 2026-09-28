import math

def normal_pdf(x, mean, std_dev):
    power_val = ((x-mean)/std_dev)**2
    middle_val = math.exp(-0.5 * power_val)
    first_term = 1/(std_dev* (math.sqrt(2*math.pi)))
    return first_term*middle_val