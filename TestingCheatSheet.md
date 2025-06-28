# A rough outline of the things you can test

NOTE: all of the 'error' examples are subject to this being handled
by the code under test. Not only are some errors simply ignored,
often a bad value is assumed to have been caught earlier and thus
not handled at the current layer

- Answers for sample data
- Answers for edge cases
- Answers for random data if there is some property it should have
    -- Even vague properties might help you spot an error sooner
- Handling of null/None answer cases
- Correlated and uncorrelated variations on inputs
    -- E.g. don't only consider 'all flags false' and 'all flags true'
- Statistical properties of solution (to a suitable level)
    -- E.g distribution from an RNG
- Consistent answer for the same data (if expected)
    -- Beware of things like unstable sorts, randomness, side effects
- Different answers for different data (where expected)
- Correct answers for end-to-end in known cases
    -- Often only a trivial one is available
- Don't forget to verify error messages - does the code fail correctly?

## A Note on practical test suites

A good practical test suite has layers (like an onion) so that
you only need to concern yourself with one thing at a time.
You should not rely on the order in which tests run (state/side effects)
but you can assume that 'deeper' layers function as expected, since
their tests will verify that. Build up the tests from the small,
simple parts towards the more end-to-end elements.

Don't jam too many things into a single test function, but in practise
we do not hold with the idea of 'a single check per test'. Check a single
'element of function' using as many asserts as you need.

Lastly, in the common case of needing 'approximate' equality, upper limits
on the size of some item, or any other testing parameters, DO approach this
the same way you approach writing code - use parameters, a data class, or some
other approach so that you can easily change these in one place. I.e. do
not pepper magic numbers throughout your code for thresholds etc.

## Other things to consider

You're not aiming to test if the libraries you depend on - that's their
job. But:

1. If you're relying on undocumented behaviour, definitely test this works as expected. A newer version may act differently and you'll save heartache by catching it quickly.
2. Do consider testing that you are using the library correctly - for example validating
a simple use-case.
3. You may want to verify that needed features are present - this is strictly validation not testing, but the consequences are similar - weird errors and bugs. So we can consider it a close-counterpart and do it in the test suite.

Input files might be needed - consider testing using these, and also testing
with them 'mocked' out and replaced by simply setting up the data they contain.

Code which uses a database or network connection is a whole new class of interesting -
there are tips but we wont give them here. Search-engine is your friend if you need to do this.

Larger codes, especially those designed to run on shared hardware
(cloud, HPC) should implement check-point-and-restore function. I.e.
the code can stop and resume. Testing this is tricky, but important. In particular,
check it both generates an output that can be resumed, and that it resumes from
a pre-prepared file.
