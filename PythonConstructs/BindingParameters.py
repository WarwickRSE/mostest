from functools import partial

#Sometimes we have a function which takes some parameters, and we want to create a new function
# which has some of those parameters fixed to a specific value.
# There's a bunch of reasons why, which we won't go into because we have a specific
# use in the Newton-Raphson exercise. Instead we'll look at options for how.

def func(x, y, z):
    """A function which takes three parameters"""
    print("  Got values {}, {}, {}".format(x, y, z))
    return x + y + z  #Doing something with them...

#Now suppose we have a reason to fix z, say z=0

# We can create a new function, but we'd have to do this for every z-value we might want etc
def func_w_z0(x, y):
    return func(x, y, 0)

print("Manual approach: ", func_w_z0(1, 2))

# The partial function is a function which takes one function and returns us another (c.f. PythonConstructs/Decorators.py)
func_w_bound_z = partial(func, z=0)
print("Partial approach: ", func_w_bound_z(1, 2))


#By the way, we can do this ourselves if we wanted
# We can create a function-returning-a-function (aka a functor)
# Can you guess why it's much easier to bind either the first or last parameter (not ones in the middle) like this?
def bind_final(f, val):
    def f2(*args):
        return f(*args, val)
    return f2

new_f = bind_final(func, 0)
print("Functor approach: ", new_f(1, 2))


# FOR COMPLETENESS, we'll note that
# we could actually do similar using a parameterised decorator BUT we need two layers to do it
# and we no longer have access to the un-bound function...
# I'll leave it here, but _don't_ recommend it as an approach
def bind_final(val):   # Getting parameter to decorator
    def decorator(f):  # Creating decorator
        def wrapper(*args):
            return f(*args, val)
        return wrapper
    return decorator

@bind_final(val=0)
def func2(x, y, z):
    print("  Got values {}, {}, {}".format(x, y, z))
    return x + y + z

print("Double decorator approach: ", func2(1, 2))
