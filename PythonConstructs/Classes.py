
#We're defining a class - an entity which can hold data and (usually) do operations on it
class ExampleClass:
    #Data here belongs to every copy of the class
    #This is not _usually_ what you want
    _dragons = ['Here be dragons']

    #This function is used to 'set up' the class
    #It gets one extra argument - the class it is setting up
    #Self is _conventionally_ used to denote this
    #Notice __ again - denoting something reserved for the Python language
    def __init__(self, data):
        #Define some data the class has
        self.data = data
    
    #We can define functions for the class - actions it can perform. These also get the special 'self' first argument
    def function1(self, value):
        #Function will 
        return self.data == value

if __name__ == "__main__":
    #We need some way to indicate we want to make one of our special classes, 
    # and to make a value of this type. Using the class name like this takes care of it
    #Notice that we don't have to (in fact must not) supply that 'self' parameter
    tmp = ExampleClass(7.3)

    #Access properties:
    print(tmp.data)
    #To call class functions
    print(tmp.function1(8.3))




    #"Advanced note": why dragons?
    # Try this:
    a = ExampleClass(1)
    b = ExampleClass(2)
    a._dragons[0] = "There be dragons"
    print(b._dragons)

    #NOTE: class attributes are shared by all members. BUT if we modify them
    # things get complicated
    # If they are _mutable_ (e.g. a list) all classes have a reference to the same object
    # If they are _immutable_ (string, number, tuple etc) all classes have 'their own copy'
    # (Until the memory optimiser comes in)
    #They are usually best avoided UNLESS you have a specific reason