from SecretFunctions.OiYou import sumItems, sumItems2

#ENTRY POINT
if __name__ == "__main__":

    #In this exercise we're going to see if the tests you wrote for the sum function actually
    # catch some common errors. Don't go looking at the code!
    # I've written two broken sum functions - sumItems is very broken and sumItems2 is a bit more subtle
    # Write (or copy-paste) your tests below. In both cases you should
    # be able to detect issues with the summing code. Can you guess the sort of errors from the results?

    try:
        #Put your tests here. Here's an example call
        a = sumItems([0.1]*10)

    except AssertionError as e:
        print("Well DONE, you caught some errors!")
    finally:
        print("Try again - I promise the code is broken!!") 


    try:
        # There's some more subtle errors in this one
        #How do your tests stack up?
        b = sumItems2([0.1]*10)

    except AssertionError as e:
        print("Well DONE, you caught some errors!")
    finally:
        print("Try again - I promise the code is broken here too!!")

    # If you want some hints/'solutions' see the file Answers/GuidedExample04.md