from math import gcd

def is_even(val):

    return (int(val/2) == val/2)

def add_fractions(val1, val2):
    """Expects two tuples of num-denom """
    num = val1[0] * val2[1] +val2[0] * val1[1]
    denom = val1[1] * val2[1]
    aa = gcd(num, denom)
    return (int(num/aa), int(denom/aa))