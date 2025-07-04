# Submit samples for analysis to Analytics

Benchling has replaced one of its modules (**“Requests”**) with another new module (**“Workflow”**). To discover how to submit samples for analysis to the Analytics team using Workflows, follow this guide. 

## Grant access to Analytics to your Project
Add _Analytics_ Benchling Team to the list of collaborators in your Project to enable the analysts to access the samples you are going to register. 

1. Navigate to your Benchling **Project settings** ⚙️

2. Add the _Analytics_ Benchling team to the list of collaborators (with **"WRITE"** access) 


```{figure} ../_static/images/grant-analytics-access-to-project.png
:alt: grant access to Analytics team
:width: 80%
:align: center

```

Save edits to the settings by clicking "Done".

```{figure} ../_static/images/done.png
:alt: grant access to Analytics team
:width: 50%
:align: center

```

→ [How to add a user or a Team as collaborator in your project](https://help.benchling.com/hc/en-us/articles/9684263074445-Set-project-permissions)

## Register samples directly in your Notebook Entry

In order to register samples to submit to Analytics, you can follow a **Sub-template** created by LIMS support for this purpose. 

Follow this video to learn how to do it:

````{raw} html
<iframe width="560" height="315" src="https://www.youtube.com/embed/WB6sRFzEi8k?si=iU3P7sP4lspgbm4R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
````

_Summary of the steps:_

1. Navigate to your experiment **Notebook Entry**

2. Insert the **sub-template** "Analytical Sample Submission" in the Entry

    → You can choose between different samples storage options: **Plate**, **Box**, single **Vials**.

3. **Fill-in** the registration and inventory tables that appeared in your Notebook Entry with the required metadata.

    ```{admonition} *Note*
    :class: my-custom-admonition

    When moving samples in a Box or a Plate, please do so **row-wise** (A1, A2, A3...) as showed in the video.

    ```
4. **Copy** (Command+C / CTRL+C) the newly-registered **samples entities** from the last table

## Create a Workflow

In order to submit your newly-registered samples for analysis to the Analytics team, you need to create a Workflow and attach the samples within it. 

 ```{admonition} *Note*
:class: my-custom-admonition

The Workflows that you can submit to the Analytics team for in-house analysis are labelled with **"AC"** (that stands for "Analytics"). Check the full list of available "AC" Workflows [here](#my-list-of-available-workflows).

```

Follow this video to learn how to do it:
````{raw} html
<iframe width="560" height="315" src="https://www.youtube.com/embed/ooW07ZzWX6M?si=52D7uFrkFkHP2W4z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
````

## VERY IMPORTANT!!

When creating a workflow, **paste all the samples in one single cell** in the "AC Samples" column (as showed in the screenshot downbelow, and in the video). If you have sample-level metadata, please add them in the previous step (when you are registering the  samples in your Notebook entry). 

```{figure} ../_static/images/important-samples-in-one-cell.png
:alt: Paste samples in one cell
:width: 100%
:align: center

```

You can achieve it by using the "Paste special" button:

```{figure} ../_static/images/paste-special.png
:alt: Use Paste Special to paste all samples in one cell
:width: 80%
:align: center

```

_Summary of the steps:_

1. **Create** a Workflow of the relevant type, based on the analysis your are interested in.

2. **Select "Table" format** for your Task table

```{figure} ../_static/images/table-format-in-workflow.png
:alt: create a Workflow
:width: 90%
:align: center

```

3. **Paste** the samples entities in a **single** **AC Samples** column cell 

```{figure} ../_static/images/paste-special-into-one-cell.png
:alt: create a Workflow
:width: 90%
:align: center

```

4. **Fill-in** the remaining metadata fields.

→ Remember to specify the correct **"Project number"** and to save the Workflow in the relevant **Project folder** (the video's Project number and Project folder are used as examples).

5. Click on **"Create"**. The analyst will receive an email and therefore will be informed about your submission. 

 ```{admonition} *Important*
:class: my-custom-admonition

You will receive an email when your samples have been analyzed and the results have been added to the Output table of the Workflow.
To access the results, download the attached file.
```
```{figure} ../_static/images/download-results.png
:alt: Download results
:width: 80%
:align: center

```

(my-list-of-available-workflows)=
## List of available Workflows

This is the available list of Workflows (one for each analysis type performed by the Analytics team):

```{figure} ../_static/images/ac-workflows-list.png
:alt: create a Workflow
:width: 50%
:align: center

```

<br/><br/>

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).