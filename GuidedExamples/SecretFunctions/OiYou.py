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



