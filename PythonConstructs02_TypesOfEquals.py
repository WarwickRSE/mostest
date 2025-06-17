
a = 1
b = 1

#Same value?
print("a == b? {}".format(a == b))
# Completely the same - same type value etc
# INFO: (literally speaking a and b are two labels for the same piece of data)
print("a is b? {}".format(a is b))

b = 1.0
#Value is still the same:
print("a == b? {}".format(a == b))
# Now type is different, so a and b are not 'identical'
print("a is b? {}".format(a is b))

#Minor GOTCHA - in the first case a is b only due to optimisation
#Behind the scenes, we only need one copy of the number '1', or '28' or whatever

c = (1,2)
d = (1,2)
print("c == d? {}".format(c == d))
print("c is d? {}".format(c is d))
#My interpreter gives a different answer on the last one depending if I paste this in, or run as a script!!
#Save the 'is' keyword for when you want to be sure something is literally another reference to the same data

from numpy import nan

print("NaN is {}".format(nan))
#Important - proper Floating point has a  special value, NaN for NotANumber
#Since it is not a number, it is not equal to anything. Even itself.
#It is also not 'not-equal'
print("NaN == NaN is {}".format(nan))


