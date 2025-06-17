
def sumItems(items):

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

    #Recall what we dicussed in the introduction - what sorts of test inputs can you give?

    #Here's an example of generating a list of inputs and calling the function:

    a = [0.1]
    for i in range(10):
        a.append(a[i]*0.1) # Smaller every time
    print(sumItems(a))

    #And here's a Python hint - you can generate a list of N of the same item like this:
    b = [1.0]*10
    print(b, len(b))