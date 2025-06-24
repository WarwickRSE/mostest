# Using a Github runner

Github Free (at time of writing) gives us up to 2000 minutes of test
running (on Ubuntu, on OSX it charges at 10 mins per minute) in piblic repos.
Warning: once you activate the runner from this example, you'll trigger the tests EVERY time you push to the repo main branch, or edit a file in the web interface - this is the 'Continuous' part of continuous integration testing. You'll also get an email every time the tests fail.

While we're getting started, we recommend making a new repo. testing things locally and manually, and only then using the automated system, to avoid uselessly running down your budget.

We configure standard actions by adding a runner file in a hidden .github directory
in our repository. We've put a copy of the basic Github example in this
directory, adjusted to install pytest and run our code, called runner.yml.

We've put a sample output log in this directory, sample_log.txt. This runs some basic pytest tests against my sample repo. They all pass.

Note that we said install PyTest up there - the base environment is just raw Ubuntu (which does at least get us Python!) - but any Python packages should be installed as part of our build. If this is taking a long time, there are tools [such as this](https://github.com/marketplace/actions/setup-python) to cache dependencies.

## Step by Step

Here's how we suggest getting started:

1. Create a new public repo on Github. You can set up with the readme if you like, or not
2. Clone that and commit some code to test, and some tests for it. Make sure this runs locally using pyTest
3. Push the result
4. On Github, go to Actions and in the Left bar hit 'New Workflow'. Under the text is a link for 'Skip this and set up a workflow yourself'. Follow this link
5. That should have created a file in the correct directory but with no content. Paste in the content of sample_runner.yml
6. Scroll down that file to where it says 'name: Run PyTest' This is the part that runs the tests. Edit the second line to match how your tests run in step 2
7. Hit the big green 'Commit changes' button. This should both commit the file, and trigger the workflow to run
8. Go to Actions again - you should now see a non-zero count for workflow runs
9. If the run failed, expect to get an email. Ask for help debugging if you can't spot what you did wrong

At this point, you're done with the basics. You can add more steps, look into more complicated recipes, or whatever you want

## Useful Things to note about the yml file

Notice the section in the yaml file marked 'on': this
controls what actions will trigger the workflow. In this sample
we've left the basic example of pushes or pull-requests on the main branch only. You can probably guess how to adjust this part!

You can add additional jobs, or you can add steps to the existing job.

You can name the jobs, name the workflow etc

The Github Marketplace has a bunch of pre-created flows for all sorts of things

## Other useful notes

By the way, to check your runner usage, go to 'Top right profile pic menu' -> Settings -> Billing and licensing -> usage
