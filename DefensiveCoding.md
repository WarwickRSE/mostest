# Defensive Coding for Research

Defensive coding, or programming, is basically just trying to
anticipate and avoid potential failures. In cases where high-reliability
is crucial, it leans towards handling failure and using redundancy
and verification strategies to mean that failures never 'leak' into
the real world.

In research codes, our aims and abilities are a bit different - there's
whole classes of error which we really can't do much to prevent. For example,
in a physics simulation, an atomic weight of 1000 being input is probably not intentional,
but we have very little insight into where to put in a cut-off.

## Suggested Strategies

Here's some of the general principles we suggest for good, robust code (or at
least, code where, when it does go wrong (it probably will) you can still
say "I did my best" )

### Failing is better than getting it wrong

Unlike safety or time critical systems, research code is rarely in a situation
where it must not fail (in the sense of exit with an error). In fact, in
nearly all cases a researcher would far prefer an error message than either
a wrong answer, or a waste of time (and money if using cloud or shared resources,
or if you pay for your own electricity).

### Warn, don't Fail, for the Unexpected

Contrary to the previous idea though, is that sometimes it is
better to _warn_ of an issue, but allow the code to carry on anyway.
Here we want to distinguish between "this code will certainly get
a wrong answer in this case" and "this potentially violates some
assumptions we have made, but may give a useful answer anyway".

For an example of the latter, consider a function to do numeric
integration. We probably want to set a limit on the steepness
of a function, since we'll get very inaccurate results for rapid changes.

So in these "borderline" cases we have a few choices:

- show a warning and carry on anyway
- show a warning and require some action to carry on
- show a warning and require re-starting with an override flag set

Usually, one of those is the right one and the consequences, cost to user and
likelihood of error say which to pick.

### Do not normalize deviance

Contrary to the previous one, we recommend against 'normalizing deviance'. A common
cause of serious accidents, this refers to making it 'normal' to ignore a warning or
exceed a limit,
making it more likely that a warning will be automatically dismissed in a case where it should
be recognized, or a limit drift far beyond where it would ever be set in one go.

If your code warns somebody every time a parameter is 'a little bit big'
they will get used to ignoring and dismissing that warning. If your docs tell
somebody "if you get X error, just turn up Y threshold" then they will be prone
to keep on turning up the dial.

Distinguish between Errors, Warnings and just plain Info, and present things to 'your user' with an appropriate label, and you'll help to mitigate this.

## Proper terms

Here are some of the more formal ideas and terms used to discuss this sort of thing.

### Side Effects and Re-entrancy

Side-effects are anything a function does other than read data and produce a
new return value - any printing, any changes to global state or internal state,
any mutation (change) to the function's arguments which can be seen after the function
finishes.

We should probably explain that rather clumsy final sentence, because Python is a little unusual in
how function arguments are handled. Most languages pass things to functions either by value
(inside the function we have a completely independent copy) or by reference (inside the function
we have a new temporary name for an existing piece of data). Python is... neither. It can be
described as 'pass by assignment' because what happens is the same as when you do 'a = b'.

What that means, is that simple data will be copied, as will immutable (not modifiable)
things like tuples. But lists will effectively be passed by reference, just like ```list1 = list2```
gives us two names for the same data, rather than a complete copy.

So in Python, passing a list to a function and modifying it is a side-effect producing operation, but passing a number and modifying it is not.

The opposite of a function with side-effects is often called 'pure' - all it does
it read its arguments and produce a return value. In performance-focused compiled
languages like C++ these functions can sometimes even be evaluated at compile-time,
and replaced with just their result.

Somewhere in the middle between side-effecting and pure is what's called 'idempotent':
a function or action where performing it several times is the same as once.
For instance, a = a + 1 is not idempotent, but a = 3 is. No matter how many times
we do it, the end state is the same.

Re-entrancy is not directly related to these, but the concepts overlap.
A re-entrant function is one which can be stopped, and then started again (from the beginning)
and still succeed. Pure functions are by definition re-entrant - they don't affect any
internal or external state, so we can interrupt them without issue. Side-effecting functions _can_ be
re-entrant, but are less likely to be, and it has to be carefully proven.

As an example, consider:

```
def set_list(lst):
    lst.clear()
    lst.append(1)
    lst.append(2)
    lst.append(3)

def append_to_list(lst):
    lst.append(1)

def new_list_with_append(lst):
    lst2 = copy.deepcopy(lst)
    lst2.append(1)
    return lst2

def show_list(lst):
    print(lst)

```

Of these, only the 3rd one (new_list_with_append) is truly pure - has no side effects and doesn't change
its arguments. The first two have side-effects but only local ones (they affect the arguments
they are passed, and nothing else). set_list and new_list_with_append are both idempotent:
if we call them again with the same inputs we get no further modifications. The 4th one (show_list) I believe is not idempotent, but I think it might depend on the exact definition
in use, and it definitely has side-effects.

By the way, the following function does not end up having side effects because of the details of how Python lists work (we re-assign the name, rather than act on the data):

```
def try_to_set(lst):
    lst = [1, 2, 3]
lst = []
try_to_set(lst)
```

### Pre and Post conditions and Invariants

Most checks we might put into our functions fall into one of three categories:

- 'Preconditions' - things which must be true when a function is called
- 'Postconditions' - things which a function guarantees will be true after it runs
- 'Invariants' - things which must always be true.

These formal terms describe what is called 'programming by contract' - a function contracts
to meet the post-conditions as long as you, the caller, meet the pre-conditions. Invariants are mostly used as a property of objects or data, rather than functions directly,
but functions are expected to maintain them.

These ideas are almost certainly familiar, if not the words. Preconditions are what you
put in your docs (you do write docs, right?) about the values (and in Python the types) a function expects to be given.
Postconditions are the things your function promises to do. An example of an invariant can be
as simple as "this class representing absolute Temperature guarantees to always have a value greater
than or equal to 0", or "this class representing a fraction will always be in its simplest terms".
As you can probably infer, there are tons of invariants, and which ones are useful depend on
the context.

## How does this play alongside testing?

Pure functions are great when we come to testing them:
we pass a value and get a result, and we get the same result for the same inputs.
Side-effecting functions are harder - if they depend on any global state
then we need to constrain this when running the test. Idempotent functions
are somewhere in the middle - if they can be repeated with the same effects
they can't depend on global state, or really modify it. So we need
to take some caution, but we don't need to carefully 'mock-up' a bunch
of state.

Moreover, functions which affect global state really ought to be tested under
all possible global circumstances - and you can see how the number of combinations
of that might rapidly multiply.

On the other hand, when we're writing tests for code, especially if
we approach it from a true 'unit testing' angle, where
we test every single function individually, it can look
like we should be inserting checks for everything everywhere.
This is a mistake - not only will we be doing un-necessary work
in cases where our checks all pass, we can accidentally make our
code _too_ fault tolerant. Because, by definition, 'fault tolerant'
code is tolerant to faults, our code can end up continuing in cases
where it ought to have stopped.

In some languages, we need to aggressively raise errors - in Python
we can mostly just decline to catch them. So, for example,
do not catch exceptions unless you can actually handle them,
in the sense of fixing the problem and carrying on.

Finally, all that stuff about pre/post conditions are invariants are
the keys to writing your tests. You set up something that meets the pre-conditions
and then verify the post-conditions. Sometimes you also set-up something
that violates the pre-conditions and verify that an error is raised (if it is meant to be).
Finally, invariants can be a great source of those 'alternate angles' for testing: while they often wont cover the details, verifying
an invariant is a good 'sanity check' on a function.
