# Static website for Benchling resources at DTU Biosustain

## Description

This repository builds a static website using Sphinx.
The website contains Benchling training resources for researchers at DTU Biosustain.

## Add or edit resources using Git

If you are new to coding, follow these step to be able to edid the repository.

#### 1. Install Visual Studio Code (VS Code)
Install VS code here: https://code.visualstudio.com/download

#### 2. Open terminal and install git


#### 3. Clone repository
    git clone https://github.com/emilesi/benchling-resources.git

#### 4. Create a new branch of the repository

Go to the path where your repository is stored:

    cd repository path

Create new branch:
    
    git checkout -b your-feature-branch

Move to the new branch:

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
