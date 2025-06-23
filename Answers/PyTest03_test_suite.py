
#We've created a file called 'code_example.py' where we have put the code to test
# Write the command to import everything from it
from code_example import *

from random import random
def test_integer_roots():
    #Integer roots by expanding

    roots = solve_quadratic(1, 0, -4)
    assert 2 in roots and -2 in roots
    assert len(roots) == 2
    
    roots = solve_quadratic(1, -1, -12)
    assert -3 in roots and 4 in roots
    assert len(roots) == 2

def test_repeated_roots():
    #Repeated roots

    roots = solve_quadratic(1, -3, 1.5*1.5)
    assert len(roots) == 1

def test_zero_coeffs():

    #For now, only a test with a value - see advanced for how]
    # to check that an error is thrown as expected
    roots = solve_quadratic(0, 1, 0)
    assert 0 in roots

def test_complex_roots():
    # Simple case of complex root
    
    roots = solve_quadratic(1, 4, 5)
    assert len(roots) == 2
    assert (-2 + 1j) in roots and (-2 -1j) in roots

def test_zero_root():
    # Checking how function handles coefficients being zero

    roots = solve_quadratic(5, 6, 0)
    assert len(roots) == 1 and 0 in roots

def test_extreme_roots():

    # Very big and very small

    roots = solve_quadratic(1*1e10, -1*1e10, -12*1e10)
    assert -3 in roots and 4 in roots
    assert len(roots) == 2    

    roots = solve_quadratic(1*1e-10, -1*1e-10, -12*1e-10)
    #assert -3 in roots and 4 in roots  #<--- risk of not quite getting an integer
    assert len(roots) == 2
    for item in roots:
        assert abs(item + 3) < 1e-10 or abs(item - 4) < 1e-10
    # See later for a handy Pytest feature to smooth this over!

def test_random():
    #Test some random non-zero coefficients for approx 0 by back-substitution

    for i in range(10):
        a = random()
        b = random()
        c = random()

        roots = solve_quadratic(a, b, c)

        for item in roots:
            assert abs(quadratic_value(a, b, c, item)) < 1e-10
