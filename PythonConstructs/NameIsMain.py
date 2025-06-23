
#Code inside a function runs when we call the function
def function1():
    print("Function 1 running")

def function2():
    print("Function 2 running")

#Code outside of a function runs when it is encountered
function1()

#Special variable containing "name we are running under"
print(__name__)

# If we're running as 'python scriptname' it is "__main__"
if __name__ == "__main__":
    function2()