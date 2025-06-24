# An introduction to Unit Testing

## About this workshop

This workshop is an introduction to unit testing in Python, aimed at those with a mathematics
or science background. It needs Python > 3.10 or so, some built-in libraries, and the PyTest library for the second part. The third part has two options: one needs a Github account and some [Actions credits](https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions) which at time of writing are included with GitHub Free.

The Introductory 'speech' is summarised in Introduction.md

## How to use the code

Hand-on practice is the only way to get to grips with the details of writing good tests. As workshop attendees may have very
different levels of experience in Python (and in programming), the examples here start very simple
but they do get hard by the end.
We have marked the 'harder' ones with a '*' in the list below - you may wish to skip these for now and come back later.
We've also marked the introductory ones with a '!' - you may wish to skip these entirely if you are familiar with Python already.

Otherwise we recommend starting at the beginning, working through the examples, asking plenty of questions, and exploring anything you aren't sure about thoroughly.
To avoid committing you to using any particular way of running Python (one of us might still prefer Vim in a terminal) we have supplied simple code files/scripts. If you prefer notebooks, you can use these for the first half, but we strongly recommend using a command-line for the second part.
Each file has 'ENTRY POINT' marked somewhere - start at this line and follow the typed instructions
to complete the exercises.

### Guided Examples

Part 1 of this workshop is all about writing single tests - how to verify truth or falsity of conditions, what sorts of conditions you need to check, and what the 'gotcha's can be to do this

- ! 01_HelloWorld - for Python newbies, or to get the hang of how we express our exercises. Plain old "Hello World"
- 02_Asserting - using 'assert' to test for truth or falsity of conditions
- \* 03_Asserting_part2 - a bit more about assert and exception handling (you might want to skip this and come back later)
- 04_FirstTesting - writing useful tests for a first simple function
- 04A_ReallyExercisingSum - a broken sum function to check your work in the previous exercise. *Please don't look at the code in* 'SecretFunction/OiYou.py' - this is a broken sum to test you!
- 05_CheckingADifferentWay - as the title says, this exercise gets you thinking about the importance of not re-writing the same code and calling it a test
- 05A_ReallyCheckingRoots - explores an inexact root-finder, with similar problems to the previous exercise
- 06_NegativeSpace- 'negative space' is the things a code shouldn't do - and it's important to test these as well as the things it should
- \* Advanced 07_TDD_lite - a quick exercise in Test Driven Development, with a nice Easter-Egg if you're interested in early computers. The "CDC 6600" was a super fast computer in the mid 60s!
- \* Advanced 08_FloatingPoint - some extra stuff about numbers which can be important in real situations
- \* Advanced 09_CoveringTheBases - why testing every line of code still doesn't make you certain

### PyTest Examples

Part 2 of this workshop uses PyTest to build a real Test Suite out of simple tests similar to the ones we wrote in part 1. Once we start to put them together, we need a more systematic way of running
them and recording the results. Testing libraries also tend to offer 'more advanced' checks in a streamlined form, adding 'syntactic sugar' - doing things which we could do within Python in a way which is clearer and more indicative, and 'sweeter' to use.

Before tackling the exercises below, you will need to install PyTest. The first exercise will check
that it is running correctly.

- test_01_first_run - a basic test, just to make sure you've got things working
- test_02_selecting - how to run only a specific function (for quick hacky tests)
- test_03_test_file - separating tests from code, and putting the tests we wrote before into the suite
- test_04_next_steps - from here you're on your own - the task is to write a test suite for the given code from scratch
- \* test_05_pytest_features - a quick walkthrough of some of pyTests extra features

### Further Reading

The folder Python constructs contains files describing some constructs that you might want to know more about, especially for the more 'advanced' parts. Dip into these if needed, or if the exercise points you to them.

- Name - what does that \_\_name\_\_ idiom actually mean?
- IdentityVsEquality - some details of how '==' and 'is' work, especially for non-basic types
- BindingParameters - more information on how we can create a function which calls another but with some parameters given pre-chosen values
- Decorators - how to write your own Python decorator, and what they do
- Class - how to write and use your own simple class (useful for the PyTest section)
- With - what the 'with' construct means, and what it does

A couple of other documents are also included in this repo.

- UsefulTerms - a small glossary (extremely incomplete)
- DefensiveProgramming - some notes on the idea of 'programming to avoid errors' and how this interacts with testing

### Automatic Testing

The third and final part of this workshop is about automatically running tests, and some guidance
is in the Automagic folder.
