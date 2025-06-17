# Answers, tips and hints

This file contains (some) answers and considerations for the exercise.

## Tests you could have run

The obvious test here is to generate a list of numbers and compare against the intrinsic 'sum' function. If you did this, _very clever_ but not entirely in the spirit of the workshop! Imagine the function was less trivial - what sort of values could you look at?

We can start by using a known answer - for instance the number 1, repeated. `[1.0]*100 -> 100`

We can explore edge cases - `[0.0]*100 ->100` or `[]->0.0`

We should check negative numbers work `[0.1, -0.1]*10 -> 0.0`

The previous answer is an example of using 'known properties of the functionality' (note the intended function, NOT the code I wrote). For instance, sum from 1 to N of [1, 2, 3, ...] is (N * N+1)/2

We should look at very small and very large values.

We could use some other things we know from maths, such as the fact that the sum of 1/2^n is 2 and if we stop at N then the answer is 2-1/2^N

We might even want to check against 'bad inputs' such as not providing a list at all, or providing a list of non-addable items. My test function wont handle these - you can explore this idea more in the advanced section on Test Driven Development.

## Things you should consider

