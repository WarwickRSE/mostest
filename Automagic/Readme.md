# Integration Testing

Integration testing refers to testing when code is 'integrated'
aka made part of, a given code base. You're more likely to hear this
as one half of the phrase 'Continuous Integration' (CI) testing - doing this every
time code gets merged, and originally ideally at least once per day.

In research codes, we rarely have anything useful on such short time
scales, but we can still do an approximation to CI testing. In this section we'll look at how.

## The one BIG pre-requisite

**Any sort of continuous testing like this needs a test suite which runs in a few seconds at absolute most.**

This is going to be happening every time you commit, merge or push, depending on setup. That means you **wil** eventually start skipping it
if it takes long enough for you to initiate a skip before it completes.

A lot of the time we need tests that simply cannot run this fast and there is no simple answer to the dilemma. The best strategy we can offer is to do super basic CI testing supplemented with scheduled extended testing, either at certain times, or on certain actions. For example, you might run some 'sanity' checks, such as 'does this code even run' (or in compiled languages, compile) all the time, and then run a suite
of comprehensive tests on every release.

## Workshop Options

Running this workshop for those familiar with Github, with Github accounts, and for so long as Actions credits stay free, we can do true CI testing. Alternately, we can setup some local testing, which isn't
quite as automatic, but is very easy, cost free, and a very good start!

### Local Automatic testing with Git hooks

Git has the ability to do things when you take certain actions, such as perform a commit. These are called hooks, because they 'hook' into what is happening, and do not require you to include them into your workflow.

The file hooks_instructions.md dsecribes how to set up a simple git hook to run a test suite before allowing a commit.

### Automatic CI testing with Github Actions

The file runner_instructions.md walks though setting up a basic Github runner to run some tests under Pytest.
