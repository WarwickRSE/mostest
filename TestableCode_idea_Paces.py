
# Program to answer the question:
  #  If I run a 10km race at an average pace of 10km/hour, have I definitely also
  #  completed a 5km single stretch at 10km/hour? What about 3km? What about 8km?

  # Simplifications - allow instantaneous pace to be random number between 0 and 1, i.e. average about 0.5 (yes this makes me a terrible runner)
  # If it holds for this, it should hold for random weaker variations about an average, and should also hold for systematic ones
  # Discretise into N distance bins
  # Use simple averaging instead of integration
  # Express the shorter distance being explored as a fraction of the total

# Strategy: 
# Generate a set of instantaneous paces, such that the average is correct
# Take every contiguous sub-set of length sub-length and calculate the average over it
# Check that there is at least one value from the previous step which is better than the overall average

# Examples - if this explanation is not clear, these might help:
#I run a bit under 10kph for the first half and a bit over for the second half, averaging exactly 10 kph - in the second interval I must cover at least 5k. Thus I have run 5k at better than 10 kph in a single stretch
# No matter how we slice it, that always holds - if the first half distance is slow, the second half must be fast and vice versa. 
# Obviously if I run 5km at 20kph, have a 30 minute nap, and then finish the second half, I might be mad, but I still must have completed 5 km continuously at (much) better than 10kph (c.f. the 1904 Summer Olympics, napping on the course)
# However, in that last case, I did NOT cover 8km at >10kph, because of the wasted 30 mins in the middle. In fact, my average pace climbs for the entire second half - at 45 mins I have covered only 5 km (~6.66 kph), and by 48 mins only 6 km (8 km in 48 minutes being 10kph)

# IMPORTANT *****
# This is not necessarily GOOD code to solve this problem
# This is code designed to challenge you to test the functions involved!
# It may be a bit un-pythonic, clumsy or tedious. Sorry about that!
# But we wanted it to be easily testable!

from statistics import mean
import random

#Create and fill list of length N with numbers between 0 and 1
def fill_inst_pace(N):

  inst_pace = []

  for i in range(0, N):
    inst_pace.append(random.random())

  return inst_pace

#For given list inst_pace, generate all contiguous sublists of fractional length sub_dist
def get_sub_paces(sub_dist, inst_pace):

  assert(sub_dist <= 1.0 and sub_dist > 0.0) #Here assert is being used to check a necessary condition for this function to work! How might you test this?
  N = len(inst_pace)
  sub_sz = int(N*sub_dist) 
  sub_upper = int( N - sub_sz) # Starting index for the last chunk of len sub_sz
  sub_pace = []

  for i in range(0, sub_upper-1):
    #All possible sub chunks of length sub_dist
    sub_pace.append(inst_pace[i:i+sub_sz])

  return sub_pace

# Calculate the average value of each sub-list in the given list
def average_sub_paces(sub_paces):
  
  averages = []
  for item in sub_paces:
    averages.append(mean(item))

  return averages

#Create a list of instantaneous paces of length N and check that each one has a contigious sub-list
# of fractional length sub_dist such that average(sublist) >= average(whole list)
def create_list_and_check_subsections(N, sub_dist):

  inst_pace = fill_inst_pace(N)

  av_pace = mean(inst_pace)

  sub_paces = get_sub_paces(sub_dist, inst_pace)
  sub_avs = average_sub_paces(sub_paces)

  sub_flags = [s>av_pace for s in sub_avs]
  
  if not True in sub_flags:
    print("Averaged ", av_pace, sub_avs)


  return True in sub_flags


def main():

  # Inputs
  N = 500  # Number of time points
  trials = 100  # Number of repetitions of check
  sub_dist = 0.8  #  Fraction of total distance to investigate

  # How often to print to screen
  display_frac = 10

  # Output - how often our assumption is violated
  fails = 0

  for i in range(trials):
    if i%display_frac == 0: print(i/trials*100, '% done')
    # What comment can I put here that says more than the code does?
    if not create_list_and_check_subsections(N, sub_dist):
      fails = fails+1

  # Check count of failures
  if(fails > 0):
    print("Trial FAILED")
    print(fails/trials*100, " % failed")
  else:
    print("Trial SUCCEEDED")

if __name__ == "__main__":

  main()




