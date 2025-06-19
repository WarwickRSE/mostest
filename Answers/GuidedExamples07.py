#This is (a) version of tests and code for the exercise
# This runs in about 7 seconds on my Macbook

_n = 5

# A helper function checking for odd or even
def is_even(n):
    return (int(n/2)*2 == n)

# The target function. Given a value, val, is it
# the nth power of any integer?
def is_nth_power_of_int(val):

    # If val isn't even an integer, it's power can't be
    if int(val) != val:
        return False
    # For odd powers, negative values can't have integer roots only imaginary
    if not is_even(_n) and val < 0:
        return False

    guess = val**(1.0/_n)
    prospective = int(guess)
    # Might be a bit under or a bit over!

    return val in [(prospective -1)**_n, prospective**_n, (prospective+1)**_n]

# All the tests I thought of
def test_all_cases():

    # Really obvious cases
    assert(is_nth_power_of_int(2**5))
    assert( not is_nth_power_of_int(2.5**5))

    # Zero is usually a good edge case
    assert(is_nth_power_of_int(0))

    # Getting to large values
    assert(is_nth_power_of_int(150**5))
    assert(not is_nth_power_of_int((-1)**5))  # This one tripped up my first code attempt!

    assert(not is_nth_power_of_int(150**5 + 0.1))
    assert(not is_nth_power_of_int(150.01**5))


# Actually answering the conjecture
def search_for_counter():
    min=1
    max = 150

    for i in range(min, max):
        for j in range(i, max):
            for k in range(j, max):
                for l in range(k, max):
                    sum = i**_n + j**_n + k**_n + l**_n
                    if is_nth_power_of_int(sum):
                        return (i, j, k, l, sum)
    return None

if __name__ == "__main__":

    test_all_cases()

    result = search_for_counter()
    if result:
        approx_rhs = int(result[4]**(1.0/_n))
        print(result, approx_rhs)
        if (approx_rhs -1)**_n == result[4]:
            rhs = approx_rhs -1
        elif approx_rhs**_n == result[4]:
            rhs = approx_rhs
        elif (approx_rhs + 1)**_n == result[4]:
            rhs = approx_rhs + 1
        else:
            rhs = None
        print("Solution found: {} {} {} {}, {}".format(result[0], result[1], result[2], result[3], rhs))
    else:
        print("No solution found")
