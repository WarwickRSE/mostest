# ADVANCED - this exercise assumes you're happy writing larger pieces of Python code
# If you're short on time, leave this for now and consider coming back another time


#ENTRY POINT

#Test driven development is the process of creating code by writing a test FIRST
# and then writing the code to pass it
# In industry, or as a consultant programmer, this is powerful - if the customer agrees
# with (or even provides) the tests, and the tests pass, you get paid
#The big challenge is writing a test suite that is complete enough that 'passing the tests'
# actually means 'doing the job'

#For example, suppose you are asked to code a phone book app, and given a test which requires
# it to handle "Joe Bloggs" on 0118 999 881 3 . Rather than design a database, you hard code this
# and only this value. Do you get paid? (I know sombody who did almost this, and yes, they did)

#However, the perfect is the enemy of the good in some cases. The fact that our tests might leave
# space for failure doesn't mean we can't try. So let's try. Or rather, you can try. Plan to spend no more than about 15 minutes on this task. 

#Write a program following https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-72/issue-6/Counterexample-to-Eulers-conjecture-on-sums-of-like-powers/bams/1183528522.full
# to disprove Euler's conjecture that if x_1^n + x_2^n + ... + x_m^n = x^n then m >= n

# In other words, find 4 numbers x_1, x_2, x_3 and x_4 in the range [0, 150] such that their 5th powers sum to a 5th power
#This is both very simple (exhaustive search on the domain [0 to 150] for each x, and n=5
# and a little bit tricky.
#You will need to write something to verify whether a number y is x^5 for any integer x
# You CAN"T just raise it to the power 1/5th numerically. 
#Write some tests for such a function
# Then, write the function

#If you like, you can write the rest of the code to do the exhaustive search
# (and if you're smart, you might notice that while the x's can all be the same, you need
# not check the order permutations, which speeds things up rather!)
# My obvious Python runs in about 7 seconds and is available in Answers/GuidedExamples07