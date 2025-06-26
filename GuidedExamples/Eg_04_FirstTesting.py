
def sumItems(items):
    # A pointless function to sum a list using a loop
    # This is terrible Python, but it's just here as an example function to test
    sum = 0.0
    for item in items:
        sum = sum + item
    return sum

#ENTRY POINT
if __name__ == "__main__":
    #In this exercise we're going to test a function to calculate the sum of a list of numbers
    # Ignore the fact that there is a built-in function to do this, and that the code I have
    # written is not very good. We're testing it, not critiquing!

    #Write your tests below for the 'sumItems' function

    #Recall what we discussed in the introduction - what sorts of test inputs can you give?

    #Here's an example of generating a list of inputs and calling the function to get started:

    a = [0.1]
    for i in range(10):
        a.append(a[i]*0.1) # Smaller every time
    print(sumItems(a))

    #And here's a Python hint - you can generate a list of N of the same item like this:
    b = [1.0]*10
    print(b, len(b))

    #YOUR CODE HERE - write your tests for the function below
    # If you're really stuck and want some hints/'solutions' see the file Answers/GuidedExample04.md but we suggest writing your own and doing the next exercise first!