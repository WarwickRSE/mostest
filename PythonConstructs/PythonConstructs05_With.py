
#ENTRY POINT
# This file is a continuous script. It is not a model of how to write nice code, it's just an exercise!

# RESOURCE MANAGEMENT
# The 'with' construct (called a context manager) is used to manage resources (e.g. a file, a database, a socket) and make sure
# they are cleaned up when the block ends. You'll probably see it used with files, to make sure they
# are closed even if an error occurs. At core, the 'with' statement will call a special function (__enter__()) at the start and another (__exit__) at the end. These are often mostly the same as the constructor
# and destructor of the class. The exit function will be handed information on any errors that have been raised, so the cleanup can be done properly.

#Here's an example

class ResourceManagingClass:

    def __repr__(self):
        return self.resource # Showing us the state

    def __init__(self):
        self.resource = "Resource Available"

    def __del__(self):
        if self.resource:
            # Do some clean-up
            self.resource = "Resource Cleaned Up" # Mark as no longer usable

    def __enter__(self):
        #Starting the block - notice the return
        self.__init__()
        print("Constructed a resource")
        return self
    def __exit__(self, type, value, traceback):
        #Gets told the type and value of an exception if the block is exiting due to one
        self.__del__()
        print("Cleaned up")
        return True

with ResourceManagingClass() as myRes:
    print(myRes)
    
    #raise ValueError # uncomment this to exit badly from the block, noting that we still see 'Cleaned up' when we do

#Use your imagination - based on this description, what and how does the following code do?

class ExceptionSwallower:

    def __repr__(self):
        return "Nom nom nom"

    def __init__(self):
        pass

    def __del__(self):
        pass
    def __enter__(self):
        #Starting the block - notice the return
        self.__init__()
        return self
    def __exit__(self, type, value, traceback):
        print("I got an exception of type {} and value {} and I ate it.".format(type, value))
        handledAllTheErrors = True 
        return handledAllTheErrors #Return value of this function should be the answer to question "did I handle the error(s)?"

with ExceptionSwallower() as it:
    print("Doing some thing")
    raise ValueError("Tastes Bad")
