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
    git clone https://github.com/biosustain/benchling-resources.git

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

    
    **Custom directives**

- create **hidden text boxes** using *{dropdowns}* (a practical use case for FAQs). 
Example:

    ````
    ```{dropdown}  Dropdown title
    Dropdown text
    ```
    ````

- create **highlighted text boxes** for warnings and tips using *{note}*, *{tip}*, *{important}*, *{warning}*, and *{caution}*. Example:
    
    ````
    ```{tip}
    Tip text
    ```
    ````

- embed an **image** as a *figure* (you can add captions to it). The image must be saved in ../_static/images/
Example: 
    ````
    ```{figure} ../_static/images/data-storage.png
    :alt: Diagram showing the meaning and relationship between Registry, Inventory and Results
    :width: 80%
    :align: center

    *The Registry, Inventory and Results*
    ```
    ````

- embed a **document**, available for download. The document must be saved in ../_static/files/. Example: 
    `````
    {download}`Strain_Template_YourName.xlsx <../_static/files/Strain_Template_YourName.xlsx>`
    `````
Alternatevely: 
    `````
    [Download Material Order Guide (PDF)](../_static/files/material_order_guide.pdf)
    `````

- preview a **pdf file** directly in the page. The document must be saved in ../_static/files/. Example: 

    `````
    <iframe src="https://docs.google.com/gview?url=https://biosustain.github.io/benchling-resources/_static/files/material_order_guide.pdf&embedded=true" width="100%" height="600px"></iframe>
    `````
- **open a file in another tab** in the browser. The document must be saved in ../_static/files/. Example: 

    `````
    <a href="../_static/files/material_order_guide.pdf" target="_blank">Open Material Order Guide in a new tab</a>
    `````

- embed a **video**. Note: certain parameters after the link are important: "rel=0&modestbranding=1&autoplay=0&showinfo=0". Example:
    `````
    ````{raw} html
    <div style="text-align: center;">
    <iframe 
        width="560" 
        height="315" 
        src="https://www.youtube.com/embed/xKyDvrNoZh8?si=ltnVty38KMEbLJxY?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
    </iframe>
    </div>
    ````
    `````

- **highlight** a phrase. You can choose any color in HEX format. Example:
    ```
    Here you will find <mark style= "background-color: #C5DBEC;">step-by-step tutorials and short training videos</mark>.
    ```

- create **textboxes** with custom background color, highlight and titles. 

    **Create custom admonition**

    First, add the following code to the file _static/custom.css. Remember to change the **name** (my-custom-admonition).
        
        `````
        .admonition.my-custom-admonition {
            background-color: #e0f0ff;
            border-left: 4px solid #0077cc;
            padding: 10px;
        }
        `````

    **Apply custom admonition**

    Add the **name** of the custom admonition: 
        
        `````
        ```{admonition} My Custom Title
        :class: my-custom-admonition

        This is a custom textbox with a custom color.
        ```
        `````

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

Mia test: editing from new computer
