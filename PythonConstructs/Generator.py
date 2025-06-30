# Generators are a kind of function that can generate
# (what a surprise) data item by item. They can use
# internal stored state to do this, but should be describable
# in some sense as 'get the next item'

# In other words, these are how we write our own constructs
# which work like 'range'

# A generator to give the letters of the alphabet
def get_alphabet():
    _aa = 'abcdefghijklmnopqrstuvwxyz'
    _n = 0  # Starts at 0, (a)
    while _n < len(_aa):
        yield _aa[_n]   # Special keyword - this is the value you get out
        _n = _n + 1

# Using the generator
for letter in get_alphabet():
    print(letter, letter.upper())

# A SILLY thing to do - create a list
# This is not pointless, but generators are usually a way to _avoid_
# having to have the entire sequence available at one time
# (Question: do you see how this makes my example pretty dumb, given how I store the letters already...?)
alph = list(get_alphabet())
print(alph)
