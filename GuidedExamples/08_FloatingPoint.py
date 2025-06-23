import sys
import numpy as np
import matplotlib.pyplot as plt

#ENTRY POINT

if __name__ == "__main__":

    #Python tries to be helpful, especially with integers, by using as much
    # storage space as needed to store an integer. These extremely-long
    # integers can be convenient, but they can introduce unexpected performance
    # costs, since the underlying computer hardware doesn't support them directly (natively)

    #On the other hand, even python doesn't do much with floating point accuracy:

    # Look at what this prints:
    a=1.0
    for i in range(1, 100):
        a = a * 10.0
        print(a, a - 10**i)
    
    #and notice that once `a` gets big enough, it's close to, but no longer exactly, the expected number. Even though things can get very large, we only have about 15 places of accuracy

    print("----------------------------------")
    # By the way, the range of floating point numbers is:
    print("Min and max floats are: {} {}".format(sys.float_info.min, sys.float_info.max))

    print("Exceeding the max: max * 10 = {}".format(sys.float_info.max*10))

    #If you want to see more about how inf, and the mysterious NaN (not a number) behave, try https://gist.github.com/hratcliffe/a48cd8cb03c98c897d6d4564ad55c402


    print("----------------------------------")
 
    #Usually, we don't worry about small errors. But consider tracking something moving very slowly
    # being tracked very far away, over a short interval

    time = np.linspace(0, 1, 100)
    x_0 = 1e14
    distance = np.linspace(x_0, x_0+1, 100)

    # This is linear, i.e. the velocity is constant:
    print("velocity is {} m/s".format((distance[-1] - distance[0])/(time[-1]) - time[0]))

    # But instantaneously:
    av = 0.0
    zeros = 0
    for i in range(1, 100):
        inst = (distance[i] - distance[i-1])/(time[i] - time[i-1])
        av = av + inst
        if inst < 1e-10: zeros = zeros + 1

        print("Instantaneous velocity is {} m/s".format(inst))
    
    print("Averaged instantaneous velocity is {} m/s".format(av/99))
    print("{} of the samples were approximately zero".format(zeros))

    print("Error in average is {} %".format((av/99 - 1.0)*100 ))

    #So we have no error on the whole period, but the instantaneous value is definitely wonky
    last_v = (distance[1] - distance[0])/(time[1] - time[0])
    accel = []
    for i in range(2, 100):
        vel = (distance[i] - distance[i-1])/(time[i] - time[i-1]) 
        print("Acceleration is {} m/s/s".format((vel - last_v)))
        accel.append((vel-last_v)/(time[i] - time[i-1]))
        last_v = vel

    # Optionally, plot the 'acceleration' - change False to True if you want to
    if False:
        plt.plot(accel)
        plt.show()

    #Now this is a bad way to find velocity, and a worse way to find acceleration. 
    # We should probably fit the position curve or something, and
    # finding derivatives on noisy data is a known-hard problem, but the gist is:
    # taking small differences on large numbers is dangerous

    print("----------------------------------")
 

    # Here's another classic 'gotcha' (in most languages this will also apply to integers)
    # Also note the brackets!
    for i in range(20):
        print("i is {}. 10^i is {}. 10^i + 1 is {} and the difference in those is {}".format(i, 10.0**i, 10.0**i + 1.0, (10.0**i + 1.0 ) - 10.0**i))

    print(" -------------------------- ")
    # Eventually, we reach a point where the next representible number is more than 1.0 bigger
    # This is called the epsilon
    for i in range(15, 20):
        print("i is {}. 10^i is {}. 10^i + 10 is {} and the difference in those is {}".format(i, 10.0**i, 10.0**i + 10.0, (10.0**i + 10.0 ) - 10.0**i))

    #On my machine, this one has a difference of 16.0 at i=17

    # It is important to keep in mind that the value of epsilon varies with the base number and
    # the thing commonly called epsilon is the value near 1.0









   