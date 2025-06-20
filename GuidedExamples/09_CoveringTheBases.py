
#Coverage testing refers to checking whether every line of code in a file
# has been executed as part of a tes
# One would like to think that this means the lines have been tested.
# This example shows how that is NOT the case

# Calculating coverage is both simple (run the tests and check every line
# ran at least once) and quite difficult (packages are either not great
# or are proprietary)
# so we're not going to try and cover doing it right now. 
# 
# Instead, in this example we're going to be deliberately, perhaps comically,
# bad at our job, to illustrate that coverage helps, but only if you are
# careful with your tests!

#Your challenge: write some tests which definitely _run_ every line of the following functions
# but also do nothing to verify their correctness
#Be creative! Try and write something which looks  lot like a test, and yet.... flops

#To check this, we provide two imports, containing the same functions, but one correct and one broken
# They contain identical lines of code except for some important changes introducing errors such as
# off-by-one, flipped comparisons etc. 
# Your goal is for your tests to find no errors in either the correct or the broken code, while looking like an actual functioning test suite
# This is (hopefully) a bit of fun, but has its roots in a very real idea called 'mutation testing' -
# checking that a test suite actually detects broken code

#The functions to check are:

#is_even(val) - whether the given (assumed integer) value is odd or even
# add_fractions(val1, val2) - takes two tuples like (numerator, denominator) and adds them. Returns a fraction (in lowest terms)

from SecretFunctions import examples
#from SecretFunctions import examples_broken



