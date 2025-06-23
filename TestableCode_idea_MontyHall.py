# This code 'checks' the Monty Hall problem (see wikipedia for details)
# Given 3 doors, two containing goats and one a car, a contestant chooses a one. 
# The host now reveals a goat (important - thereby introducing new information)
# Is the contestant better to stick with their first choice or swap to the other option?

#Variations on the problem use more initial doors, one car, and have the host reveal all but
# 2 doors - the one the contestant originally picked, and one other, with one of these two
# guaranteed to be the prize

#We're going to generate a bunch of random setups, random reveals and calculate the probability of winning

import random

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

def run_trial(n_doors, swap):
    """Run a single realisation of the game with n_doors doors, and contestant strategy swap = True or False"""

    # Better verify we have at least 3 doors
    assert(n_doors >= 3)

    # Swap is whether the contestant will decide to swap doors

    doors = generate_door_layout(n_doors)
    cp = contestant_pick(doors)
    hp = host_pick(doors, cp)

    if swap:
        # Find whichever door is not already chosen, or selected by the host
        available_doors = range(1, n_doors+1) # Start with all possible door indices
        # Account for host having revealed possibly more than 1
        new = [i for i in available_doors if i not in hp and i != cp] 
        assert len(new) == 1, "Host did not reveal enough doors!"
        cp = new[0]

    return doors[cp-1]

def run_sim(trials, n_doors, swap):
    """Run 'trials' iterations of the game, with the given number of doors and contestant strategy"""

    wins = 0
    for i in range(trials):
      win = run_trial(n_doors, swap)
      if win: wins = wins + 1
    return wins

if __name__=="__main__":

    nt = 10000
    nd = 3 # Usual problem is 3 doors

    swap_wins  = run_sim(nt, nd, True)
    stick_wins = run_sim(nt, nd, False)

    print("Won {} of {} times ({} %) by swapping".format(swap_wins, nt, (swap_wins/nt * 100)))
    print("Won {} of {} times ({} %) by sticking".format(stick_wins, nt, (stick_wins/nt * 100)))
