# There's a good chance you have already met the idea of exceptions
# as soon as you try and use a dict, or take the log of a negative
#number. Exceptions are a kind of error-message designed to
# bubble-up through code until something deals with them - in
#other words, you have to explicitly 'cancel' the error, it
# will not just get lost.
#

# 'Catching' an exception is also known as 'handling' it
a = {}
try:
    b = a['keyThatDoesNotExist']
except:
    # Do something useful - perhaps
    # tell 'the user', perhaps
    # set b to some meaningful default value, etc
    print("Using default b!")
    b = 1

#Sometimes we want to catch only a specific type
# This also shows how to grab the exception into a variable
# to do things with it

try:
    b = a['-1']
except KeyError as e:
    print("Key error: ", e)


# Producing an exception is also known as throwing or raising
# You can do this yourself manually, although perhaps it is
# better to have them produced by letting an operation fail
# "naturally"

try:
    raise ValueError("I am an exception (to prove the rule?)")
except Exception as e:
    print(e)


# Sometimes we want to add information about an error
# but we CANNOT fix it - we want it to continue to
# bubble. In this case we should 're-throw' or 're-raise' it

try:
    b = a['aKeyINeed']
except Exception as e:
    print("Key is missing - did you forget to run the 'fill_inputs' function")
    #raise e

#Comment out the raise e line above to run the rest of the code!

#Sometimes we want to do something in case there were NO errors:

try:
    b = a.get('someKey', 10)
except Exception as e:
    print(e)
else:
    print("B set successfully to {}".format(b))

#Lastly, sometimes we want to do something regardless of their being errors
# For example, perhaps we want to close a file, but know that reading from
#it might produce errors - we can do something in every case like this:

try:
    b = a[-1]
except Exception as e:
    print("Error: ", e)
finally:
    print("I got to this part of the code, even if I did fail on the way")


