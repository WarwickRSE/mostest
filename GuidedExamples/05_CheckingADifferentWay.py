from math import sqrt
def quadratic_value(a, b, c, pt):
    #The value of ax^2 + bx + c at x = pt
    return a*pt*pt + b*pt + c

def solve_quadratic(a, b, c):
    #find the roots of the equation ax^2 + bx + c = 0 where a, b and c are real

    roots = []
    disc= b*b  - 4.0 *a*c
    if(disc >0):
        sqrt_d = sqrt(disc)
    elif (disc < 0):
        sqrt_d = sqrt(-disc) * 1j  #Complex roots
        
    if(disc == 0):
        roots.append(-b)
    else:
        roots.append( (-b + sqrt_d) /(2.0*a))
        roots.append( (-b - sqrt_d) /(2.0*a))
 
    return roots


#ENTRY POINT
if __name__ == "__main__":

    #When testing simple code it can be tempting to just repeat the same task
    #However, there's a high chance we're going to make exactly the same mistake
    #(In fact, I have heard of people literally copy-pasting the code into the test...)
    #So we need to find a different angle. In real cases, this probably ends up with us
    # having to do a bunch of 'not quite perfect' checks, and hoping that we don't
    # miss any edge cases. This is perhaps the biggest challenge to effective testing

    #Let's start simple. 
    # Write some tests for the quadratic root finder above.
    # Consider - what defines a root?
    # What cases might there be?
    # What range of values might you want to explore?

    # Here's an example call:
    print(solve_quadratic(1, -1, -1))

    # There's some hints on the 'solution' in the file Answers/GuidedExample05.md