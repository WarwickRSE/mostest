def myFunction():
    """This is a docstring - a special line interpreted as a description of the function.
    It also counts as the body of the function"""
    # A function containing only comments isn't valid! - the docstring above lets me leave this empty for you to fill in without causing confusing errors if you run it first

    #In Python, the 'try' 'except' construction is used to 'catch' errors so that we can
    # do something useful with them. 

    # Write a try-except block. In the 'try', put an a
    try:
        assert(False) #Will cause an assertion error
    except Exception as e:
        print("An error occured: ", e)


if __name__ == "__main__":

    myFunction()