# An introduction to Unit Testing

## About this workshop

....

## How to use the code

Hand-on practice is the only way to get to grips with the details of writing good tests. As workshop attendees may have very
different levels of experience in Python (and in programming), the examples here start very simple
but they do get hard by the end.
We have marked the 'harder' ones with a '*' in the list below - you may wish to skip these for now and come back later.
We've also marked the introductory ones with a '!' - you may wish to skip these entirely if you are familiar with Python already.

Otherwise we recommend starting at the beginning, working through the examples, asking plenty of questions, and exploring anything you aren't sure about thoroughly.
To avoid committing you to using any particular way of running Python (one of us might still prefer Vim in a terminal) we have supplied simple code files, with __TBC!!!__ an ipynb version too.
Each file has 'ENTRY POINT' marked somewhere - start at this line and follow the typed instructions
to complete the exercises.

### Guided Examples

Part 1 of this workshop is all about writing single tests - how to verify truth or falsity of conditions, what sorts of conditions you need to check, and what the 'gotcha's can be to do this

- ! 01_HelloWorld - for Python newbies, or to get the hang of how we express our exercises. Plain old "Hello World"
- 02_Asserting - using 'assert' to test for truth or falsity of conditions
- \* 03_Asserting_part2 - a bit more about assert and exception handling
- 04_FirstTesting - writing useful tests for a first simple function
- 04A_ReallyExercisingSum - a broken sum function to check your work. **Please don't look at the code in** 'SecretFunction/OiYou.py' - this is a broken sum to test you!
- 05_TestingIsNotDoingItAgain - as the title says, this exercise gets you thinking about the importance of not re-writing the same code and calling it a test
- 06_NegativeSpaceTesting - 'negative space' is the things a code shouldn't do - and it's important to test these as well as the things it should
- \* Advanced 07_TDD_lite - a quick exercise in Test Driven Development
- \* Advanced 08_FloatingPoint_extras - some extra stuff about numbers which can be important later
- \* Advanced 09_CoveringTheBases - why testing every line of code still doesn't make you certain

### PyTest Examples

Part 2 of this workshop uses PyTest to build a real Test Suite out of simple tests similar to the ones we wrote in part 1. Once we start to put them together, we need a more systematic way of running
them and recording the results. Testing libraries also tend to offer 'more advanced' checks in a streamlined form, adding 'syntactic sugar' - doing things which we could do within Python in a way which is clearer and more indicative, and 'sweeter' to use.

Before tackling the exercises below, you will need to install PyTest and check you can run it. 

- 01_BasicExample - a basic test, to make sure you've got things working
- 02_ASimpleTestSuite - using the tests from before in the new system
- 03_TestableCode - now you're on your own - write a test suite for the given code from scratch
- \* Advanced 04_InterestingPyTestFeatures - suggestions for tackling more interesting avenues in testing

### Python Constructs

Some files describing some constructs that you might want to know more about, especially for the more 'advanced' parts. Dip into these if needed, or if the exercise points you to them.

- PythonConstructs01_name - what does that \_\_name\_\_ idiom actually mean?
- PythonConstructs02_TypesOfEquals - some details of how '==' and 'is' work, especially for non-basic types
- PythonConstructs03_class - how to write and use your own simple class (useful for the PyTest section)
- PythonConstructs04_with - what the 'with' construct means, and what it does
