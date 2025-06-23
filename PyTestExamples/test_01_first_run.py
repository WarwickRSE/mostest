
#ENTRY POINT

#As a first go with PyTest, lets re-run some of the simple tests from before but
# using the nicer test runner

#PyTest will gather all the functions from the file we give it, run them, and give
# us a nice summary.

#Here's my really dumb example to prove that we're running pytest correctly!
# Run the command `pytest test_01.py`
def test_test_runner():
    assert(True)

def test_test_runner_failing():
    assert(False)

# Add a few more functions here, some which pass, some which fail
# One BIG advantage of using PyTest is that it doesn't exit on the first
# big error - we can get all the results at once