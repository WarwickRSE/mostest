from functools import partial

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

    # Insert some tests here to verify that the newton_raphson code above works 'in general' and gets the right answer

    #Your tests will hopefully flag up some cases where the simple code above fails. We'll revist this in the next example with a more 'cautious' code where I have tried to protect against common issues in the inputs