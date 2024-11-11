# Benchling resources at DTU Biosustain

## Description

This repository builds a static website  containing Benchling resources created at DTU Biosustain.

The website is built using [Sphinx](https://www.sphinx-doc.org/en/master/usage/index.html) and [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Add or edit resources using Git

If you are new to coding, follow these step to be able to edit the repository.

#### 1. Install Visual Studio Code (VS Code)
Follow instructions here: https://code.visualstudio.com/download

#### 2. Open terminal and install git
Follow instructions here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 

#### 3. Clone repository
    git clone https://github.com/emilesi/benchling-resources.git

#### 4. Create a new branch of the repository

Go to the path where your repository is stored:

    cd repository path

Create new branch:
    
    git checkout -b your-feature-branch

Check in which branch you are now:

    git branch 
(you should see an asterisk (*) next to your-feature-branch, indicating you are currently on that branch)

Open repository in VS Code:

    code .

#### 5. Edit files within VS Code

- edit the "About" section in `about.md`
- edit or add articles in `folder_topic/article_topic.md`
- update the `index.md` file to include new files
- use [pandoc](https://pandoc.org/try/) to convert your existing training files into markdown or reStructuredText

#### 6. Push changes to GitHub

Go back to your terminal and stage your changes:

    git add .

Commit your changes with a descriptive message:

    git commit -m "Description of your changes"

Push your new branch to your GitHub repository:

    git push origin your-feature-branch

#### 7. Create a Pull request

Open your web browser and navigate to your GitHub repository.
You should see a prompt to create a Pull Request for your recently pushed branch. Click on *Compare & pull request*.
Fill in the title and description for your Pull Request, explaining what changes you made and why.
Click Create pull request.

In the Pull Request, you can mention specific people to request reviews by typing @username in the comments section.

## To consider for following editing 

Before editing again, run these commands to pull new edits from the Main and merge them to your branch.

Switch to the Main branch

    git checkout main

Pull changes from Main branch

    git pull origin main

Switch to your branch

    git checkout your-feature-branch 

Merge the latest changes from main into your feature branch:

    git merge main

Note: If you need to access your GitHub account from the terminal, you might need [an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## Build the site locally to enable site preview in VS code

While being inside the folder containing your local repository, install required packages from requirements.txt:
    
    pip install -r requirements.txt

Build the site locally by running the following command:
    
    sphinx-build -n -W --keep-going -b html ./ ./_build/

If this doesn't work, run the following:

    python -m sphinx -n -W --keep-going -b html ./ ./_build/

Now you should be able to see the _build folder in VS code.

To enable the preview of the site in VS code, install the extension "Live Preview" in VS code.

To preview the website, right-click on index.html and click "Show Preview".