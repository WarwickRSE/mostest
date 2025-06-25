#ENTRY POINT
import pytest

from os import environ

#So far, we have stuck to assert-ing things - numbers, sizes, types etc.
# But there's lots of other tasks that we might want to tackle, and if
# we want to be able to do something, chances are other people do too. 

#This file contains simple examples of some of the useful 
# things PyTest can do

#We're going to apply them against the same code_example.py we used earlier
from code_example import *

#Firstly, that root finder is able to raise an exception - the 'quadratic' equation 0x^2 + 0x + 2 has no roots. See the following:
if __name__ == "__main__":
    # NOTE: pytest ignores this block
    try:
        roots = solve_quadratic(0, 0, 2)
    except ValueError as e:
        print(e)

# We can check that an exception is (correctly) raised like this:
def test_no_roots():

    # Demand that this case raise an exception, specifically a ValueError
    with pytest.raises(ValueError):
        roots = solve_quadratic(0, 0, 2)
    # If you want to know _how_ this block works, see PythonConstructs/With.py
    # Do note that you can't do anything AFTER the exception occurs - the code after that
    # will not be run

# We can mark tests to be skipped, or skipped on a condition
# Change False to True to skip this one and clean up the  test output
@pytest.mark.skipif(False, reason = "Because it fails")
def test_which_definitely_fails():
    # This one shows what happens if your code does NOT raise the expected exception

    with pytest.raises(Exception):
        assert True

#If you need to do something more complicated, you can capture info on the exception like this:

def test_which_checks_exception():
    dic = {}
    with pytest.raises(KeyError) as exc_info:
        print(dic['the_wrong_key'])
    # The type and message can be looked at:
    assert exc_info.type is KeyError
    assert exc_info.value.args[0] is 'the_wrong_key'


# The other thing we've already done is to compare numbers, but approximately
# There's a function (strictly speaking a class) for that
#(This defines a special '==' operator which compares with 'a fuzz' -
# either 1e-6 times the value given, or a number you specify)

from math import pi
def test_approx_value():

    # Passes:
    assert pytest.approx(3.14159) == pi
    #Fails
    #assert pytest.approx(3.16) == pi

    #Note the '==' operator is defined to work both ways round, so also:
    assert pi == pytest.approx(3.142, 0.1)

# We can capture output to screen (stdout and stderr), and to files
# and examine it as part of tests
def function_which_prints():
    print("Hello World")

def test_which_prints(capsys):

    # This function prints something:
    function_which_prints()
    # This grabs back what was printed
    captured = capsys.readouterr()
    assert "Hello" in captured.out

# We can run tests with parameters, although we need some way of creating the parameters. A simple case is one where we want to run a test for numbers from 0 to 5:
@pytest.mark.parametrize('val', range(5))
def test_with_params(val):
    assert val < 5

# You can see that this will be run with the values 0...4 using the 'dry-run command'
#  pytest --co test_05_pytest_capabilities.py