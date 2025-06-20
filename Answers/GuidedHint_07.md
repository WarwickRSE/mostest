# A hint for solving " does y = x^n for any integer x"

There may be sophisticated ways to do this, but we don't
need to get too clever. We have two obvious choices.

The first one is to recognise that we can't do y^(1/n) because (for example)

```

>>> 100000**0.2
10.000000000000002
>>> 100001**0.2
10.000019999920001
```

and both have some trailing digits. We can't, in general, decide whether
there is 'too much' for this to be an integer, and if we try, we're likely
to be wrong. But we do now know that if x does exist, it is close to 10.
Rather than try and prove something, we can just cover the possibilities -
we check 9^5, 10^5 and 11^5 and see if one is exactly equal to y - job done.

The alternative, especially if exponentiation is costly, which it was on early computers,
is to form the list of x^n for the x's, which for our brief here of x up to 150, is both
small to store and cheap to search. Then we simply look up y in this list, which we can
search quickly (binary search etc) and if y is not there, then it is not an n-th power.
