from math import sqrt
def quadratic_value(a, b, c, pt):
    #The value of ax^2 + bx + c at x = pt
    return a*pt*pt + b*pt + c

def solve_quadratic(a, b, c):
    #find the roots of the equation ax^2 + bx + c = 0 where a, b and c are real

    # Special cases:
    if a == 0 and b != 0: 
        return [-c/b]
    elif c == 0:
        return [0]
    elif a == 0 and c!= 0:
        #Bad - no solution
        raise ValueError("Quadratic with 0x^2 + 0x + c has no roots")

    roots = []
    disc= b*b  - 4.0 *a*c
    if(disc >0):
        sqrt_d = sqrt(disc)
    elif (disc < 0):
        sqrt_d = sqrt(-disc) * 1j  #Complex roots (Python uses 'j' for sqrt(-1))
        
    if(disc == 0):
        roots.append(-b)
    else:
        roots.append( (-b + sqrt_d) /(2.0*a))
        roots.append( (-b - sqrt_d) /(2.0*a))
 
    return roots
