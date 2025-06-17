from math import pi
#ENTRY POINT
if __name__ == "__main__":

    #This will succeed
    assert(True)
    #This will raise an error and the program will exit. Uncomment it, run this program and see
    #assert(False)

    #Values such as 1 are 'truthy' (evaluate as true). 0 is 'falsy' - evaluates as false. Later we will see some other 'falsy' values

    a = 1

    #Use the 'assert' function to verify that a is 1

    #Now try 'assert'ing something untrue - what happens?

    b = 1.0

    #Before running it, try and decide what 'a == b' will assert as
    # Now check it

    #What about 'a is b'? What is different?


    name1 = "Alice"
    name2 = "Bob"
    #Use 'assert' to check these are different strings:

    #Now check their lengths are different using assert:


    #OPTIONAL:
    #Using 'assert', identify some other 'falsy' values - values which cause
    # an assertion error. 0 is such. What string value is there? What can you put in a list so that assert(my_list) throws an error?


    #CORE
    #Make sure you're happy with the other sorts of things you can put inside 'assert' by writing
    # the code for the true and false cases of the following expressions
    c = 3.14

    # Example:
    # c is at least 3 -> assert(c >= 3) (successful) assert(c < 3) (fails)

    #Case A: c is strictly greater than 3

    #Case B: c is NOT zero

    #Case C: c is within 0.5 of the value 3 (c is in the range [2.5, 3.5])

    #Case D: c is within 0.01 of the value of pi (note we have `from math import pi` up above)

    #Case E: c squared is less than 10

    #Case F (Optional, tricky if you dont know how): c is a whole number (integer)
