from SecretFunctions.helpers import * # polynomial and polynomial_deriv like the previous example, and a fixed Newton-Raphson
from functools import partial

from math import sqrt

def velocity_from_kinetic_energy(ke, mass):
    """ K.E. = 1/2 m v^2 - this inverts this to calculate v from a given KE and mass"""

    return sqrt(ke*2.0/mass)

def ordinal_number(num):
    """ Ordinal numbers are like 1st, 2nd, 3rd, 4th etc. This takes a number and returns this string """

    if num%10 == 1 and num%100 != 11:
        return "{}st".format(num)
    elif num%10 == 2 and num%100 != 12:
        return "{}nd".format(num)
    elif num%10 == 3 and num%100 != 13:
        return "{}rd".format(num)
    else:
        return "{}th".format(num)

#ENTRY POINT
if __name__ == "__main__":

    #Until now, we have largely been focusing on testing values, and making sure our
    # functions do the thing they claim to do correctly
    #But we haven't really considered testing the 'bad' cases - verifying that our code
    # correctly fails or rejects bad values.

    #We're going to look at a few 'mechanical' checks first, then we'll revisit the newton_raphson code in a 'defensive' form

    # 'Negative space' in art is when you draw an object by shading everywhere it is not.
    # Negative space testing is a lovely picturesque description of the idea of testing the things
    # our functions should not do - e.g. the inputs it should reject and the cases in which it should fail

    print("A 1kg object with a kinetic energy of 50J is moving at {} m/s".format(velocity_from_kinetic_energy(50, 1)))

    # What should this function do if it is passed a negative energy? What about a negative mass? It should fail:
    try:
        print("A 1kg object with a kinetic energy of -50J is moving at {} m/s".format(velocity_from_kinetic_energy(-50, 1))) 
    except Exception as e:
        print("Test failed successfully with ERROR: ", e)
    else:
        # This part runs only if we DID NOT get an error
        print("I expected that to fail!")

    try:
        print("A -1kg object with a kinetic energy of -50J is moving at {} m/s".format(velocity_from_kinetic_energy(-50, -1))) 
    except Exception as e:
        print("Test failed successfully with ERROR: ", e)
    else:
        print("OOOPS! Are you SURE that's physically meaningful?")

    #So in this case, our function as written does something meaningless. We'd really rather catch that! So can you go fix the function to raise its own error (instead of relying on sqrt to do it?)

    #We'll come back to how to write a test to ensure something throws an exception when we come to PyTest later. For now, just have it print message like we do up there.

    #Once you've fixed that, let's consider some other things we might want to demand, and how we can
    # then ensure they do not slip through
    try:
        print("Well done! You came {} in this race!".format(ordinal_number(3.14)))
    except Exception as e:
        print("Test failed successfully with ERROR: ", e)
    else:
        print("OOOPS! Are you sure that's a countable number?")
    # Unless it's competitive pi-eating, I doubt that sentence above is what we intended!
    # Can you add a test for the 'ordinal_number' function to check that it only accepts
    # integers, and then fix it to pass your test? (Note - it's up to you what you think
    # 1.0 should do - can you see how to both allow or reject it?)


    #Now let's consider what the newton-raphson code can do wrong. We've imported a copy of polynomial and polynomial_deriv already, as well as the partial function we use to set the coefficients
    #And we've imported a 'fixed' version which traps the common errors. Either here, or in the 05A file, re-run your tests against the fixed version
    # Hint - the cubic with coeffs = [1.0, -1.1/3.55, -0.765/3.55, 0.74/3.55] and guess = 5/9 may surprise you!

    #After running the tests you already wrote, try and think of all the 'negative space' we might want this function to find and reject. Write some tests to check any you think of
    
    # Finally, compare the two implementations. Did you catch the same issues that I did? If I missed any, feel free to let me know!



    #FINAL NOTE on this example: In this example we have been examining the question of testing, and
    # I have provided some functions which do a lot of checking internally.
    # This is not always the right thing to do.
    # Every check costs time, and it is not always clear how 'defensive' our functions should be
    # Do not take this example as an exhortation to add every check you can think of into every function!
    # Aim to strike a balance between explicit checks, clear code, and performance!!
    # The file DefensiveCoding.md has some more thoughts on this