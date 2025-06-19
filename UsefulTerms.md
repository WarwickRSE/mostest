# Useful Words and Ideas

This Document contains a list of some of the terms you might not have previously heard,
along with quick descriptions. We like to be precise, so sometimes we put somthing in square-
braces \{like this\} when we think it is not terribly helpful right now, but might
be important to you later.

## Numerics Terms

Some of these are probably very familiar!

-Associative: an operation which comes out the same in any order in the sense that a+b+c = a+(b+c) == (a+b)+c
-Floating-point: the normal way non-whole numbers are stored in the computer. A lot like scientific form (a x 2 ^ b) but notice the 2 instead of the usual 10.
-32 and 64 bit, aka FP32 and FP64: the number of bits (0 or 1) used to store. Usually 32 bits is divided as TBC and 64 bits as 1 for sign, 11 for the exponent (including +ve and -ve values) and 52 for the mantissa
    - FP16, FP8 and even FP4 show up in Machine learning contexts! Less bits -> more flops \{Floating Point Operations Per Second - the base measure of performance \}!

## Python/Programming Terms

-Scope: the area of a program where a variable exists. In Python, only functions limitscope - i.e. a variable created inside a function can't be used outside of it. Beware though:as variables can be used only after they have been set, code like "if False: x = 10" can lead to trouble
-Mutable: objects in Python are either mutable - i.e. they can change value, or immutable - i.e. they can't. Don't confuse this with being able to refer to a new value using an existing name! For example 'a = [1, 2, 3], a[0] = 0' changes the list [1, 2, 3] into the list [0, 2, 3]. 'a=(1, 2, 3), a =(0, 2, 3)' stores first a value (1, 2, 3) (a tuple, and immutable) and then a new value (0, 2, 3). Mutable vs immutable matters most when passing things to functions, and when copying them, as the two sorts behave a bit differently.

## Testing Terms

- Unit Testing: testing the individual functions in a piece of code separately
- The "Competent Programmer" hypothesis: rarely named, but widely relied on, this is roughly the idea that mistakes in code tend to be small (or else they're rapidly spotted) and thus big errors only sneak in by combining several smaller ones
- Continuous Integration Testing: continually testing the whole code every time it changes. This usually means doing it automatically. Originally 'continuous' meant 'almost as soon as you write something tangible, and at least daily' but this is often relaxed
- Test Driven Development: a development style summmarised as "first write a test. Then write the code to pass it. Repeat as necessary". Extremely powerful in cases where you _can_ write a test which dictates correct or incorrect code, but beware: an apparently simple condition in words might not map to simple code: "identify all non trivial zeros of the Riemann zeta function"
