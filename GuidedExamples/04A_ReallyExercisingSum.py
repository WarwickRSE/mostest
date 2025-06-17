from SecretFunctions.OiYou import *

if __name__ == "__main__":

    try:
        #Put your tests here. Here's an example call
        b = sumItems([0.1]*10)

        # Some more subtle errors in this one
        c = sumItems2([0.1]*10)

    except AssertionError as e:
        print("Well DONE, you caught some errors!")
    finally:
        print("Try again - I promise the code is broken!!") 