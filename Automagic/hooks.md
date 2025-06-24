# Using Git Hooks

Git hooks are simple scripts which git (which is just a program)
will run when you take certain actions. For example, a runnable
script called 'pre-commit' in the special hidden folder .git/hooks

**DO NOT DELETE or modify things in the .git folder** - this contains all of the stuff git
needs to track your code history! Only modify things in the .git/hooks folder specifically.

We've put a sample hook script in this directory, called pre-commit. This is just a bash/shell script. If you don't know any shell scripting,
please do ask. For the most part these are the same as 'the commands
you would type' but there's some things we need to be able to check
success and failure for the hook to work.

## Step by Step

Here's how we suggest getting started:

1. Create a new repository in a new folder. Call it anything you like
2. Commit some code to test, and some tests for it. Make sure this runs manually using pyTest
3. Copy the file 'pre-commit' from this directory into the folder .git/hooks in that repo, and make it executable (```chmod u+x <filename>```) (see footnote)
4. Edit that file to match your environment setup (my example uses a venv called 'env', yours may not). To check this works, you can simply run the script
5. Edit the file to run the tests correctly
6. Attempt to commit. If the tests pass this should work as normal
7. Write a failing test and verify that the commit does not proceed

Footnote: this script assumes the bash shell at /bin/bash. Fix that if
you want another shell or program, ask for help if you're not sure

## Other Hooks

The .git/hooks directory contains some examples of a bunch of different hooks.
The content can be a bit impenetrable, but the filenames give a good indication
of the tasks git can hook into.
pre-commit, pre-push and pre-merge-commit are probably the most useful ideas.
