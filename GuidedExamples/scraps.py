def myFunction():
    """This is a docstring - a special line interpreted as a description of the function.
    It also counts as the body of the function"""
    # A function containing only comments isn't valid! - the docstring above lets me leave this empty for you to fill in without causing confusing errors if you run it first

    #In Python, the 'try' 'except' construction is used to 'catch' errors so that we can
    # do something useful with them. 

    # Write a try-except block. In the 'try', put an a
    try:
        assert(False) #Will cause an assertion error
    except Exception as e:
        print("An error occured: ", e)

def host_pick_3(doors, contestant_pick):
    # In general the host can reveal any number of doors - this is the version relying on there being 3 doors, and thus only 1 to reveal
    # They never select the one the contestant has selected, NOR the one with the prize

    #NOTE: if we want this to be properly "fair" for the statistics we need to be careful
    # I do not promise I have been careful enough, although I think I have

    n = len(doors)
    assert n == 3, "Not implemented bigger problems yet"

    prize = doors.index(True) + 1
 
    #Pick random non-prize, non-contestant selected door:
    # This eliminates either 1 or 2 doors from those the host could pick
    # One if both conditions are the same door
    if prize == contestant_pick:
        choice = random_pick(n-1)
    else:
        choice = random_pick(n-2)

    # Choice is the index into the 'available' doors - ones which are
    # neither a prize nor the contestant's pick (remember both properties may be the same door!)
   
    # [g, g, c, p, g, g]
    # [1, 2, -, -, 3, 4] # Available doors marked
    # [g, p, g, c, g, g] #
    # [1, -, 2, -, 3, 4]
    # [g, p/c, g, g, g, g]
    # [1,  -,  2, 3, 4, 5] #One more available since prize is same as contestant's pick

    # Skipping over 'disallowed' doors
    # Note - this is just fixing the index to avoid the '-' in the arrays above
    # We are not changing the host pick here
    # We could alternately do something like:
    # available_doors = [1, -, -]  # could also look like: [-, 1, -] or [-, 1, 2]
    # Choice is 1 in first two cases and either 1 or 2 in the last one
    # choice = available_doors.index(choice) + 1
    while(choice == prize or choice == contestant_pick):
        choice = choice + 1

    return [choice]





if __name__ == "__main__":

    myFunction()