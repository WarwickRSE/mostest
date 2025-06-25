import pytest
from TestableCode_idea_MontyHall import *

from math import floor
import os
from uuid import uuid1

# ----------- Testing random pick ------------------------------

# This will run 5 times - and we can just not use the repeat_count param in the test
@pytest.mark.parametrize('repeat_count', range(5))
def test_random_picker1(repeat_count):
    N = 10
    a = random_pick(N)
    assert a >= 1 and a <= N

def test_random_picker2():

    # It's a wrapper on an RNG, what can we really test?
    # Check the average return is (N +1)/2...
    sum = 0
    for i in range(100):
        sum = sum + random_pick(10)
    
    assert sum/100 == pytest.approx(5.5, 0.25)

# Here are some tests which fail!
@pytest.mark.skip(reason="These Fail in the code as written")
def test_random_picker_failing():

    with pytest.raises(Exception):
        # This is nonsense, so might want to raise some kind of exception?
        a = random_pick(-1)

    with pytest.raises(Exception):
        # Ditto - it's an index so ought to reject non-integer
        a = random_pick(3.5)

#-----------Testing generate_door_layout -------------------

def test_layout():
    doors = generate_door_layout(5)
    assert len(doors) == 5

@pytest.mark.parametrize('door_count', [3, 5, 73, 100])
def test_layout1(door_count):
    doors = generate_door_layout(door_count)
    # Exactly one door should be true
    assert doors.count(True) == 1

def test_layout2():
    doors = generate_door_layout(3) 
    # Check doors contains only True or False
    # set -> the unique values
    door_vals = set(doors)
    assert len(door_vals) == 2 and True in door_vals and False in door_vals

def test_layout3():
    # Layout is random, so it's hard to do much. Verify that we at least get different
    # ones (this CAN fail, but the probability ought to be very low!)
    N = 100
    doors = generate_door_layout(N)
    d1 = doors.index(True)
    doors2 = generate_door_layout(N)
    max_iter = 100 # Try up ot 100 times to get a result different to the first one
    i = 0
    while doors2.index(True) == d1 and i < max_iter:
        doors2 = generate_door_layout(N) 
        i = i + 1
    assert doors2.index(True) != d1

# --------- Testing contestant_pick ----------
# For the basic version, there's very little to test, but we can repeat the
# stuff from random_pick

@pytest.mark.parametrize('repeat_count', range(5))
def test_contest_pick1(repeat_count):
    N = 10
    doors = [False] * 10
    doors[5] = True
    a = contestant_pick(doors)
    assert a >= 1 and a <= N

# For Uncle Rupert's wonderful strategy..... well. We should probably make sure
# he picks a valid door...

@pytest.mark.parametrize('repeat_count', range(5))
def test_uncle_rupert_pick1(repeat_count):
    N = 10
    doors = [False] * 10
    doors[5] = True
    a = uncle_ruperts_pick(doors)
    assert a >= 1 and a <= N


# --------- Testing host_pick ----------------
@pytest.mark.parametrize('door_count', [3, 5, 73, 100])
def test_host_pick(door_count):
    
    #Definition: Pick all but 2 doors from the given list - one will be the contestant's pick, and the two will definitely contain the prize door

    doors = generate_door_layout(door_count)
    pick = contestant_pick(doors)

    host_reveals = host_pick(doors, pick)

    # Reveals all but two
    assert len(host_reveals) == door_count - 2
    # Can't be the contestant's pick
    assert pick not in host_reveals
    for hp in host_reveals:
        assert not doors[hp-1] # Can't be the prize! 1-based indexing...

@pytest.mark.parametrize('door_count', [3, 5, 73, 100])
def test_host_pick2(door_count):
    #Once again, all we can really do is check that over time
    # the host tends to pick all the doors except the two special ones
    doors = [False]*door_count
    doors[0] = True  #Prize - remember 1-based for contestant and reveals
    contestant_pick = 2 # Contestant

    all_picks = set([])
    # Estimate how many trials to cover all the doors...
    # Probably proportional to how many there are
    for i in range(door_count*10):
        reveals = host_pick(doors, contestant_pick)
        all_picks.update(reveals)
    assert len(all_picks) == (door_count - 2)   # Covered all doors

#------------ Test swap_selection ---------

# A fixed case
def test_swap_selection():
    doors = [False]*10
    doors[0] = True  #Prize - remember 1-based for contestant and reveals
    cp = 2 # Contestant initial
    reveals = range(3, 10+1)

    new = swap_selection(doors, reveals, cp)

    # Check they have not stayed the same
    assert new != cp
    # Check they have not picked one that is not allowed
    assert new not in reveals
 
 # A full case with randomness
def test_swap_selection2():
    door_count = 15
    doors = generate_door_layout(door_count)
    cp = contestant_pick(doors)

    host_reveals = host_pick(doors, cp)
    new = swap_selection(doors, host_reveals, cp)
       # Check they have not stayed the same
    assert new != cp
    # Check they have not picked one that is not allowed
    assert new not in host_reveals 

# ---------- Test run_trial ------------
#There's really nothing we can do - this function just plugs together
# other functions. We could check the door count error case?

def test_trial():

    with pytest.raises(AssertionError):
        run_trial(2, True, False)
    with pytest.raises(AssertionError):
        run_trial(2, False, False)


# ----------- Test run_sim -----------

# We can test against the KNOWN cases, ignoring Rupert
# This is VERY unusual - that we have an analytic solution and yet
# still want to run the code
@pytest.mark.parametrize('nt, nd', [(100, 3), (1000, 3), (100, 20)])
def test_sim(nt, nd):

    wins = run_sim(nt, nd, True)
    expected = floor((1-1/nd)*nt)

    assert wins == pytest.approx(expected, 2) # Allow ± 2?

# --------- Test read_input_file -----------
# NOTE: we didn't provide good an bad input files, but sometimes testing does need them
# However our file reading code here is pretty poor, so it's not going to pass many
# good tests

# Here's some tests which reveal just how bad this code is!
@pytest.mark.skip(reason="These Fail in the code as written")
def test_reader1():
    read_input_file("FileThatDoesNotExist.xyz")

def test_reader2():
    # Creating a bad file on-the-fly
    filename = 'file_'+str(uuid1())
    with open(filename, 'w') as file:
        file.write("nt=abc")
    
    # Reader silently ignores the bad line....
    read_input_file(filename)
    # Delete our temporary file
    os.remove(filename)


# ---------- Test report_wins ----------
# This is maybe a bit pointless, but it shows HOW we can do this

def test_reporting(capsys):

    wins = 10
    trials = 100
    doors = 3

    report_wins(wins, trials, doors, False)

    captured = capsys.readouterr()
    # NOTE: using the same format statement amounts to 'doing the same thing'
    # So we insert here the entire report
    # This is NOT usually the right thing to do unless the format
    # of the report is vital!
    caps = str(captured.out).split('\n')
    assert "Ran 100 trials with 3 doors" in caps
    assert "Won 90 of 100 times (90.0 %) by swapping" in caps
    assert "Won 10 of 100 times (10.0 %) by sticking" in caps


# Testing the whole dealy-whack
# Final Stretch! Now we just have to write the test to tell Uncle Rupert
# that he can't beat the odds
@pytest.mark.parametrize('nt, nd', [(100, 3), (1000, 3), (100, 20)])
def test_rupert(nt, nd):

    #Run rupert's strategy. Find that it gives the same odds
    wins = run_sim(nt, nd, True, use_strategy=True)
    expected = floor((1-1/nd)*nt)

    assert wins == pytest.approx(expected, 2) # Allow ± 2?

if __name__ == "__main__":
    """Using this to tests the tests as I develop them"""

    #test_host_pick2(5)
    test_swap_selection2()