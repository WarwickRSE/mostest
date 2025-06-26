def myFunction():
    #In Python, the 'try' 'except' construction is used to 'catch' errors so that we can
    # do something useful about them. Sometimes we can fix the problem and try again, sometimes
    # we can print some useful information, etc

    #What will this block of code do? Run it and find out!
    try:
        assert False #Will cause an assertion error
    except Exception as e:
        # The statement above catches ANY sort of error and hands it to us in the variable 'e'
        print("An error occured: ", e)

    #Catching all errors is Very. Bad. Form. - we probably don't know what to do with some potential errors, so we should leave those for (hopefully) another part of the program to handle
    # Instead we should usually catch specific kinds of error. For instance:
    emptyDict = {} #An empty dictionary (for other-language programmers - aka map, key-value store, associative array etc)
    try: 
        a = emptyDict['keyWhichDoesNotExist']
    except KeyError as e:
        print("Key error {}".format(e)) #The {} denotes space that the format function inserts into the string
    except Exception as e:
        #This would catch any other sorts of error. Go put a different mistake into the try block and see
        print("Unknown kind of error {}".format(e)) 


#ENTRY POINT
#This example covers exceptions (errors) a little bit more
if __name__ == "__main__":

    # Go look in myFunction to see what this program does
    myFunction()