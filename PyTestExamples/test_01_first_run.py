
#ENTRY POINT

#As a first go with PyTest, lets re-run some of the simple tests from before but
# using the nicer test runner

#PyTest will gather all the functions that start 'test_' from the file we give it, run them, and give
# us a nice summary.

#Here's my really dumb example to prove that we're running pytest correctly!
# Run the command `pytest test_01.py`
def test_test_runner():
    assert True

def test_test_runner_failing():
    assert False

def this_is_not_a_test():
    pass

# Add a few more functions here, some which pass, some which fail
# One BIG advantage of using PyTest is that it doesn't exit on the first
# big error - we can get all the results at once

#Another big benefit is 'assertion introspection' - it doesn't just say that it failed
# it tells us more about what failed and why