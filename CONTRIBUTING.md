# Contributing guidelines

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

### Setting things up

To set up the development environment, follow the instructions in [README.md](https://github.com/rajat2502/StandNote#how-to-get-started-locally).

### Finding something to work on

If you find something that interests you, feel free to open an issue and we’ll help get you started.

Alternatively, if you come across a new bug on the site, please file a new issue and comment if you would like to be assigned. The existing issues are tagged with one or more labels, based on the part of the website it touches, its importance etc., that can help you in selecting one.

### Instructions to submit code

Before you submit code, please get the issue assigned to you so we know you are working on it.

We have definite branching structure, please find the details in [README.md](https://github.com/rajat2502/StandNote#github-repository-structure). To submit code, follow these steps:

1.  Create a new branch off of master. Select a descriptive branch name.

    ```
      git remote add upstream git@github.com:harshitasao/FlaskWeatherApp.git
      git fetch upstream
      git checkout master
      git merge upstream/master
      git checkout -b your-branch-name
    ```
    
2.  Commit and push code to your branch:

    - Commits should be self-contained and contain a descriptive commit message.

      ### Rules for a great git commit message style

      - Separate subject from body with a blank line
      - Do not end the subject line with a period
      - Capitalize the subject line and each paragraph
      - Use the imperative mood in the subject line
      - Wrap lines at 72 characters
      - Use the body to explain what and why you have done something. In most cases, you can leave out details about how a change has been made.

      ### Example for a commit message

            Subject of the commit message

            Body of the commit message...
            ....
            
3.  Once the code is pushed, create a pull request:

    - On your GitHub fork, select your branch and click “New pull request”. Select the relevant branch as the base branch and your branch in the “compare” dropdown.

    If the code is mergeable (you get a message saying “Able to merge”), go ahead and create the pull request. Once you are done, comment below each review comment marking it as “Done”. Feel free to use the thread to have a discussion about comments that you don’t understand completely or don’t agree with.

    - Once all comments are addressed, the maintainer will approve the PR.
    - - For further query regarding rebasing, visit https://github.com/todotxt/todo.txt-android/wiki/Squash-All-Commits-Related-to-a-Single-Issue-into-a-Single-Commit
    - Once rebasing is done, the reviewer will approve and merge the PR.

Congratulations, you have successfully contributed to Project!
