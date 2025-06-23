#from examples import *
from broken_examples import *


#Here are some tests I came up with which (I checked) my coverage suite
# claims 100% for, and yet the broken code gives me all green lights

#I've tried to make the errors not-too-obvious
# And I've written a few variations for fun

def test_is_even():
    a = 2
    assert is_even(a) or is_even(a+1)

def test_is_even2():
    a = 3
    assert is_even(a) or not is_even(a)

def test_is_even3():
    a = is_even(2)
    assert True

def test_add_frac():
    
    aa = add_fractions((1, 2), (1, 2))
    assert aa[0]/aa[1] == 1


if __name__ == "__main__":

    test_is_even()
    test_is_even2()
    test_is_even3()

    test_add_frac()