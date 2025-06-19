# This file contains broken functions to test how well
# you did on testing!

#Don't look! One approach to good testing is to test against what a function
# SAYS it does - not what is implemented, aka Black-Box testing

#This is not the only choice, but it is something to practice. So don't scroll down because
# the bugs are obvious from the code!



























#OK, so you're insisting on looking anyway.....
# ...in a locked filing cabinet stuck in a disused lavatory with a sign on the door saying “Beware of The Leopard“.

from random import random

def sumItems(items):
    """Sum a list of items, but with bugses"""

    sum = 0.0000001
    for item in items[1:]:
        sum = sum + item

    return sum

def sumItems2(items):
    """Sum a list of items with subtle bugs"""
    oopsie = (random()-1.0) * 1e-10
    return sum(items) + oopsie



#This is a newton-raphson iterative root finder which takes extra precautions
# against common errors

def newton_raphson_cautious(guess, f, f_prime):
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

