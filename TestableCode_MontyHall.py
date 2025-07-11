# This code simulates the Monty Hall problem (see wikipedia for details)
# Given 3 doors, two containing goats and one a car, a contestant chooses one. 
# The host now reveals a goat (important - thereby introducing new information)
# Is the contestant better to stick with their first choice or swap to the other option?

#Variations on the problem use more initial doors, one car, and have the host reveal all but
# 2 doors - the one the contestant originally picked, and one other, with one of these two
# guaranteed to be the prize

# TEST DATA:
# For the case of 3 doors, the odds are 66.6 % to win by swapping and 33.3 by sticking
# In fact, for any number of doors, it's 100/N % to win by sticking and 100 * (1-1/N) by swapping

import random
from datetime import datetime

def random_pick(n):
    """Pick a random item from 1 to N"""
    #Remember, this is testable code - I wouldn't usually wrap this away!
    return random.randint(1, n)

def generate_door_layout(n):
    """Create a list of length n where one random item is true and the rest false"""

    doors = [False]*n
    pick = random_pick(n)
    doors[pick-1] = True  #Label doors 1 to N so index -1

    return doors

def contestant_pick(doors):
    """Pick a random door from the given list and return its index"""

    #Note: function takes doors list not its length in case we wanted
    # more sophisticated picking. Sig. matches host_pick too which helps clarity
    return random_pick(len(doors))

def uncle_ruperts_pick(doors):
    """ Since there is no magic strategy, we've simulated Uncle Rupert by taking the middle door, unless the current clock seconds are between 0 and 30, when we take the first. This is as sane as anything and almost COMPLETELY untestable!!! Have fun """
    # See PyTestExamples/test_04 for who Rupert is...


    now = datetime.now()
    if now.second < 30:
        return 1
    else:
        return len(doors)/2


def host_pick(doors, contestant_pick):
    """Pick all but 2 doors from the given list - one will be the contestant's pick, and the two will definitely contain the prize door"""
    # In general the host can reveal any number of doors - we'll do all but ONE alternate
    # They never select the one the contestant has selected, NOR the one with the prize

    #NOTE: if we want this to be properly "fair" for the statistics we need to be careful
    # I do not promise I have been careful enough, although I think I have

    n = len(doors)

    prize = doors.index(True) + 1

    # The problem is usually stated as 'revealing N-2 goats'. However, we can more easily think of
    # it as picking one other door to 'offer' the contestant. This will NOT be the one they have picked
    # We will reveal all the others, and we will NOT reveal the prize.
    #If the contestant has already picked the prize, we shall be trying to 'bait' them with a goat
    # If they have picked a goat, we offer them the chance to win once again

    #Choosing which door the host will 'offer' the contestant
    if prize == contestant_pick:
        #Select a random goat to offer the contestant
        choice = random_pick(n-1)
        if(choice >= prize):
            # Bump index to ignore the prize door
            choice = choice + 1
    else:
        #We should reveal all but the prize
        choice = prize

    # Now open all the doors except the contestant's pick and our pick
    reveals = [i for i in range(1, n+1) if i != choice and i != contestant_pick]
    return reveals

def swap_selection(doors, reveals, cp):
    # Swap contestant's selection from what it is to whichever other they are offered
    # Find whichever door is not already chosen, or selected by the host

    available_doors = range(1, len(doors)+1) # Start with all possible door indices
    # Account for host having revealed possibly more than 1
    new = [i for i in available_doors if i not in reveals and i != cp] 
    assert len(new) == 1, "Host did not reveal enough doors!"
    return new[0]

def run_trial(n_doors, swap, use_strategy):
    """Run a single realisation of the game with n_doors doors, and contestant strategy swap = True or False"""

    # Better verify we have at least 3 doors
    assert n_doors >= 3

    # Swap is whether the contestant will decide to swap doors

    doors = generate_door_layout(n_doors)
    if use_strategy:
        cp = uncle_ruperts_pick(doors)
    else:
        cp = contestant_pick(doors)
    hp = host_pick(doors, cp)

    if swap:
        cp = swap_selection(doors, hp, cp)

    return doors[cp-1]

def run_sim(trials, n_doors, swap, use_strategy = False):
    """Run 'trials' iterations of the game, with the given number of doors and contestant strategy"""

    wins = 0
    for i in range(trials):
      win = run_trial(n_doors, swap, use_strategy)
      if win: wins = wins + 1
    return wins

def read_input_file(filename):
    """ Read some key-value items from a file"""
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    vals = {}
    for line in lines:
        try:
            segs = line.split('=')
        except:
            pass # Skip this line
        try:
            vals[segs[0].strip()] = int(segs[1])
        except:
            pass # Skip line - not an integer etc
    return vals

def report_wins(count, trials, doors, swap):

    if swap:
        swap_wins = count
        stick_wins = trials - count
    else:
        swap_wins = trials - count
        stick_wins = count
    print("Ran {} trials with {} doors".format(trials, doors))
    print("Won {} of {} times ({} %) by swapping".format(swap_wins, trials, (swap_wins/trials * 100)))
    print("Won {} of {} times ({} %) by sticking".format(stick_wins, trials, (stick_wins/trials * 100)))

if __name__=="__main__":

    #Read the inputs from file
    filename = 'MontyHallInputs.txt'
    inputs = read_input_file(filename)
    try:
        nt = inputs['nt']
    except:
        nt = 1000 # Default
    try:
        nd = inputs['nd']
    except:
        nd = 3 # Usual problem is 3 doors
    try:
        swap = inputs['swap'] == 1
    except:
        swap = True

    wins  = run_sim(nt, nd, swap)

    report_wins(wins, nt, nd, swap)

