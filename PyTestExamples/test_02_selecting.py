
#ENTRY POINT

# One obvious question you might now have is, if PyTest will run all the functions it finds
# isn't it going to run all of our code as well as the tests?
# Yup. We have two choices. For this very first example, we're going to 'cheat' and
# ask it to run ONE function, called 'test_all'. Everything else in the file will be ignored.
# This is NOT recommended as an approach, but we'll use it very briefly

# Run just the 'test_all' function like this:
# `pytest test_02_selecting.py::test_all`

# Compare the information we get here with what we got from just 'an assert failing'
# in what we were doing before. Testing tools try hard to help us diagnose what failed
# where it failed and (if possible) what was wrong.

#Now jump down to the 'test_all' function to carry on

def sum_items(items):
    # A pointless function to sum a list using a loop
    # This is terrible Python, but it's just here as an example function to test
    sum = 0.0
    for item in items:
        sum = sum + item
    return sum

def test_sum_1():
    a = [1.0]*100
    assert(sum_items(a) == 100.0)
def test_sum_2():
    a = [1.0/32.0]*32
    assert(sum_items(a) == 1.0)
def test_sum_3():
    a = [0.000001]*1000000
    assert(sum_items(a) == 1.0)

def test_all():
    """Runs all the tests"""

    test_sum_1()
    test_sum_2()
    test_sum_3()

    #Running tests like this works, but notice that to the test-suite we've asked it to run
    # ONE test with a bunch of sub-parts. This makes it a bit less clear what went wrong where
    # ALSO we can easily forget to put a test part into the list

    # SO we should really take advantage of our tools, and let PyTest collect the tests for us
    # We'll do this in the next example