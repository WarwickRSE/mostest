from functools import partial
from SecretFunctions.OiYou import newton_raphson_cautious

#For simplicity, we will assume a polynomial so we can do an analytic derivative
def polynomial(pt, coeffs):
    """Polynomial with coeffs, evaluated at val. Coeffs from highest order to lowest, any length"""
    result = coeffs[0]
    for i in range(1, len(coeffs)):
      result = result * pt + coeffs[i]

    return result

def polynomial_deriv(pt, coeffs):
    """Derivative of polynomial, same constraints as polynomial"""
    n = len(coeffs)
    result = coeffs[0]* (n-1)
    for i in range(1, len(coeffs)-1):
      result = result * pt + (coeffs[i] * (n-i-1))

    return result

def newton_raphson(guess, f, f_prime):
    """"Find a root near the guess of the equation f. f_prime should be the first derivative"""
    #NOTE: f and f_prime should accept a single argument, pt, and return the value at this point

    threshold = 1e-10 # Accuracy
    prev = guess
    diff = 1.0 # Definitely > threshold right now

    while abs(diff) > threshold:
        next = prev - f(prev)/f_prime(prev)
        diff = next - prev
        prev = next

    return next

def newton_raphson_2(guess, f, f_prime):
    """"Find a root near the guess of the equation f. f_prime should be the first derivative"""
    #NOTE: f and f_prime should accept a single argument, pt, and return the value at this point

    _max_iter = 100 # Avoid an infinite loop
    threshold = max(guess*1e-6, 1e-10) # Accuracy - related to guess but protect from 0 or too small
    prev = guess
    diff = threshold * 10 # Definitely > threshold, whatever value we might choose!
    iter = 0
    while iter < _max_iter and abs(diff) > threshold:
        next = prev - f(prev)/f_prime(prev)
        diff = next - prev
        prev = next
        iter = iter + 1

    if iter >= _max_iter:
       # Probably maxed out...
       raise RuntimeError("Max iterations {} exceeded without meeting threshold change".format(_max_iter))
    
    return next

#ENTRY POINT
if __name__ == "__main__":

    #This root finder uses an iterative approach, so there's a bit more we might want to consider
    # For example, an interative approach can loop forever if we aren't careful
    # And, we're no longer expecting an exact solution, so we need to consider thresholds again


    #First thing first - test the polynomial and derviative
    #Notice that I have used an 'optimised' calculation - this give you the opportunity
    # to use a more explicitly written one as a test while meeting the 'do it different' target
    # How might you test the derivative function?
    coeffs = [1, -1, -1]
    val = 1.68
    print(polynomial(val, coeffs))
    print(polynomial_deriv(val, coeffs))


    # Now we can test the root finder
    # Here's how to call it, passing it functions. We need to create 'polynomial with specified coefficients' to match what the newton-Raphson function. This is how:
    polynomial_with_coeffs = partial(polynomial, coeffs=coeffs)
    print(polynomial_with_coeffs(val))
    polynomial_deviv_with_coeffs = partial(polynomial_deriv, coeffs=coeffs)

    guess = -0.6
    print(newton_raphson(guess, polynomial_with_coeffs, polynomial_deviv_with_coeffs))