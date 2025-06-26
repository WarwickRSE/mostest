# Introduction

## Opener

This workshop is about testing. Most of the hands-on part is going
to be about _how_ we do this.
So before we jump in, we should make sure we understand
_why_ we are doing it, and _what_ we expect to achieve.

So, what's testing about?

1. First we assume we're smart people and sensible programmers. We have some code. We're pretty sure it's about right. It might have some errors, but we didn't accidentally write Doom when we were aiming to write a matrix inversion. We're worried we might have missed a term here, or flipped a sign there

2. Based on that, we really really hope that any BIG errors we have are built out of smaller errors. This would be super, because if we can find and eliminate the small errors, we increase our confidence in the big result

3. We CANNOT prove something is correct by testing; only that it is incorrect. This means we have to test as many pieces as we can, and ALSO test how they fit together

4. There is no magic trick. If we wrote the code right in the first place, we wouldn't need testing. Why should we expect to be any less error-prone when writing the tests? The ONLY trick we're pulling is to find two ways to do the thing and hoping that we don't do the same thing wrong twice

5. If we could truly write down what our code is meant to do, we often wouldn't need to run it,
because we would already have an analytical result. So by definition, to be novel, our code must
be doing something we cannot predict, and thus cannot test for correctness

... The End ...

At this point I guess it probably sounds like we're out of luck before we even start. We can't prove
our code is correct, and we can't even rely on our tests to be correct either. But we can _try_!

## Testing Adds Confidence

The perfect is the enemy of the good here. Just because testing can't do everything we might
want, doesn't mean it can't do anything. We just have to cover as many angles as we can,
while recognizing that this _improves_ our confidence, and reduces the space for error,
without eliminating the possibility for wrong answers or mistakes.

To do this, we put together several pieces.

- We use Unit testing (testing individual functions) to check all the little pieces work - that they do what they promise on known inputs.
- We cover as much of the domain as we can - checking big, small and zero numbers, checking big files, checking names with accents, all the inputs we can imagine.
- We use additional properties to cross-check our functions, such as invariants, or properties that the results should have regardless of how we obtained them
- Once we're confident in our functions, we put them together and try and verify that the correct bricks are making the correct building (Integration Testing, End-to-end Testing)
- Especially in the sciences and applied maths, we can use model solutions, and check our code works for a case with known answers
- Lastly, we protect our future by recording known issues, and adding checks for them (Regression Testing)

NOTE: testing like this probably wont catch the case where you have
a perfectly correct piece of software, and then apply it to the wrong
problem. Like with the Hubble Space telescope (dubbed "The most precise
error in history") you can extremely precisely do the wrong thing. In other words
testing proves the software correct, not the answer.

ANOTHER NOTE: tests should verify that a function does what it promises to,
not the details of how it is currently implemented. For example, a function
to locate an item in a list might guarantee that in case of duplicates it will
return the first instance, or the last, or just one of them. Suppose it is the
"any one of them case", but currently happens to always return the first - you should
not write your tests assuming it will always be the first, as this is an implementation
detail, not a fundamental property of the function.

## Floating Point Mathematics

Since this workshop is aimed at those with a maths background, we're going to
reveal a dirty secret of computing: there are no real numbers. There is no ⁠
𝑅. Computer floating point is not a field.

Not only is there a finite cardinality, floats/reals on the computer aren't commutative OR associative under addition and multiplication, and addition does not have an inverse operation.

If that's a surprise, it's because we use a fixed number of bits to hold our numbers, giving a finite count, and we're effectively rounding on every single operation.

Let's demonstrate - we use scientific form with 3dp for the mantissa:

```
1.234 + 1.0x10^-3 = 1.235
1.234 + 1.0x10^-4 = 1.234 

1.234 + 5.0x10^-4 + 5.0x10^-4 = ????
1.234 + (5.0x10^-4 + 5.0x10^-4) = 1.235
(1.234 + 5.0x10^-4) + 5.0x10^-4 = 1.234 
5.0x10^-4 + 5.0x10^-4 + 1.234 = 1.235 (assume left to right) 

```

Now we use way, way more than 3dp in anything we do. BUT this is still happening, down around 15 dp and it can matter!

## Example: reproducible sums

Suppose we have a list of numbers. Let's try to compute the sum of all the numbers from 0 to 1 split in 1000 increments, i.e. 0.001, 0.002 up to 1.0
We know the answer we expect for integers: it's n * (n+1) / 2. We're dividing by n throughout, so it's just (n+1)/2. For n = 1000, we expect 500.5

Generating this list and summing it gets a very close answer, on my machine good to
one part in 1e-12. But here's where it gets interesting: let's reverse this and do
the sum from end to start of the list. We get a slightly different answer.

We can do a bunch of other valid things, and that tiny error can be persuaded to almost double.

So the error is tiny, and we probably don't care about it very much. But we're trying to test
things here, so we need to decide what we will accept as the 'right' answer.

Suggestions:

- thoughtlessly compare exactly to the analytic value:
 -- never going to pass

- use a fixed threshold, for example 1e-13
 -- what if we use this function with a list of very small numbers, say around 1e-13 themselves?
 -- Numbers too small will pass this test even if the sum is wrong

- Use a fractional error
 -- A good idea, but a fraction of what?
 -- OK, a fraction of the smallest term?
  --- What if that term is 0? 1e-30?

Now in reality, reproducible sums on a high-range set of numbers are _hard_, in fact
research-grade hard. We've used it just because it's so wonderfully easy to break!
If you're interested in this problem in particular, start by looking up 'condition number'
for a sum.

## Word Ladders, or Telephone

The fact that sums are hard is not the point here. Hopefully, if high-precision sums, the ability
to difference large sums to obtain small differences etc, are involved in our project, we're
aware of this and actively working to get it right.

This is meant to illustrate the general problem that we're
already struggling to write a good robust test for a simple sum and have
had to resort to using approximate equality.

Most of the time, we're not worried about tiny errors. All we want is to be close enough, so we set a threshold for the answer. But suppose, rather than a sum, we have a complicated problem
and have to use a calculated reference solution as the 'right' answer.

Enter, telephone. Lets look at it from the side of the [word ladder](https://en.wikipedia.org/wiki/Word_ladder)

```
head
heal
teal
tell
tall
tail
```

every line differs by only one letter, and yet the first and last are completely different.

Thresholded comparisons can introduce a similar problem: we can have _a_ approximately equal to _b_ and _b_ approximately equal to _c_, yet _a_ is not approximately equal to _c_ within our threshold.

This causes a variety of problems. The one we want to particularly flag up here is that if we write a test to continuously check that a new version of a code is 'about the same' as a previous one, over time the answer can drift a very long way.

## The Light at the End of the Tunnel

Now, let's be nice and clear about the secret a lot of people wont tell you:

slapping a test suite onto your code might let you show a nice Green badge on your Github page, but
it wont fix anything.

No procedure or tool can make you do testing right. You can write completely useless tests very easily, such as simply checking if 10 ?= 10, and even tools which try and make sure every line of code is 'tested' (coverage testing) usually only make sure it's been run.

So now we've introduced a lot of reasons testing isn't going to save you, and a lot of issues
we're going to encounter with doing it well. But all is not lost.

There is one great counter-point - if you set out to write code that is testable - it is modular, it doesn't have a ton of branches (low cyclomatic complexity), your functions have one job, you catch and/or raise errors for bad inputs - you will have WRITTEN BETTER CODE!

So testing our code helps us be more confident in its correctness, AND the process
of writing tests helps us write better code, Do this thoughtfully, and you
win both coming and going.
