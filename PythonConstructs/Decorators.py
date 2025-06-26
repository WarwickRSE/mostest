# This file is a continuous script. It is not a model of how to write nice code, it's just an exercise!

# DECORATORS
# Decorators - functions which act on another function to produce a new function
# That's probably not a very helpful description, but it is accurate. Decorators
# let us wrap new function around an existing function. Best explained with an example

#For simplicity we'll do the example with a function that doesn't return anything, but
# you can 'capture' the return value and return it if needed. We'll also assume only positional
# arguments (not ones passed by name)

# Suppose we want to time a whole bunch of functions. We could put start, stop and print in at every point in our code - but what if we want to change which timer we use, or swap from printing to logging? We'd prefer to keep it all in one place.

#A boring wrapper
from time import time, sleep
def timer(original_function, *args):
    start = time()
    original_function(*args) # Call the function, passing the args
    end = time()
    print("Took {} seconds".format(end - start))

#Example function
def func(a):
    sleep(0.1) # Pause a bit
    print(a)

#We can call our function using the wrapper:
timer(func, 11)

#But now we have to do _that_ everywhere. We'd like to have just the idea of the timed function (back as a first-class function - something we can pass around, store etc)

#We can do this:
def wrap_timer(f):
    def timer(*args):
        start = time()
        f(*args) # Call the function, passing the args
        end = time()
        print("Took {} seconds".format(end - start))
    return timer  # timer is a new function, wrapping the timing around the original f
#This creates a new function which is 'f with timing'
func_with_timing = wrap_timer(func)
func_with_timing(11)

#We've got the timed function back - we can store it, call it etc. But what if we'd
# like to insert the timing when we define the function? Thats where decorator syntax comes in:
@wrap_timer
def func2(a):
    sleep(0.2) # Pause a bit
    print(a)

func2(21)

#While timing isn't a bad example of how to do this, it's not a clear winner for 
# the decorator syntax, so don't worry if that looks a super complicated way to
# do something simple. We really could just define our function, apply the wrapper and store the result
# But, among other things, that leaves us with _two_ functions, one of which we don't want people to use
# and the wrapping might get moved away from the definition
#For these (and other) reasons, the decorator syntax with '@' is preferred unless you specifically need the unwrapped/undecorated function too
#Even then, perhaps it would be 'more Pythonic' and less unexpected to define one function
#then another with decorator, like this:

def func_body():
    ...

@wrap_timer
def func_main():
    ...

# What if our wrapped function returns something? We can handle that like:
def wrap_with_return(f):
    def new_f(*args):
        # Whatever code we want here
        ret = f(*args)
        # Whatever other code we want
        return ret  #Pass on the return value
    return new_f


#By the way, we can parameterise a decorator
def print_message_before_running(message):   # Getting parameter to decorator
    def decorator(f):  # Creating decorator
        def wrapper(*args):
            print(message)
            return f(*args)
        return wrapper
    return decorator

@print_message_before_running("Function Decorated With This Message")
def func2(x, y, z):
    return x + y + z

print("Mucky parameterised decorator: {}".format(func2(1, 2, 3)))
