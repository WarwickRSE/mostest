
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

#This is a newton-raphson iterative root finder which takes extra precautions
# against common errors

def newton_raphson_cautious(guess, f, f_prime):
    """"Find a root near the guess of the equation f. f_prime should be the first derivative"""
    #NOTE: f and f_prime should accept a single argument, pt, and return the value at this point

    _max_iter = 100 # Avoid an infinite loop
    if(abs(guess) > 1e50 or abs(guess) < 1e-50): raise ValueError("Guess too big or too small!")
    threshold = max(guess*1e-6, 1e-10) # Accuracy - related to guess but protect from 0 or too small to difference
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

