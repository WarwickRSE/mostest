# Using a Github runner

Github Free (at time of writing) gives us up to 2000 minutes of test
running (on Ubuntu, on OSX it charges at 10 mins per minute).
Warning: once you turn this on, you'll trigger the tests EVERY time to push to the repo, or edit a file in the web interface - this is the 'Continuous' part of continuous integration testing. You'll also get an email every time the tests fail.

While we're getting started, we recommend making a new repo. testing things locally and manually, and only then using the automated system, to avoid uselessly running down your budget.

We configure standard actions by adding a runner file in a hidden .github directory
in our repository. We've put a copy of the basic Github example in this
directory, adjusted to install pytest and run our code, called runner.yml.

We've put a sample output log in this directory, sample_log.txt. This runs some basic pytest tests against my sample repo. They all pass.

Note that we said install PyTest up there - the base environment is just raw Ubuntu (which does at least get us Python!) - but any Python packages should be installed as part of our build. If this is taking a long time, there are tools [such as this](https://github.com/marketplace/actions/setup-python) to cache dependencies.
