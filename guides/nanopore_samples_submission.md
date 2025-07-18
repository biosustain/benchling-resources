# Submit samples for analysis to DNA Foundry

Benchling has replaced one of its modules (**“Requests”**) with another new module (**“Workflow”**). To discover how to submit samples for analysis to the DNA Foundry team (for **Nanopore GridION** analysis) using Workflows, follow this guide. 

## Grant access to DNA Foundry to your Project
Add _DNA Foundry_ Benchling Team to the list of collaborators in your Project to enable the analysts to access the samples you are going to register. 

1. Navigate to your Benchling **Project settings** ⚙️

2. Add the DNA Foundry Benchling team to the list of collaborators (with **"WRITE"** access) 


```{figure} ../_static/images/grant-dnafoundry-access-to-project.png
:alt: grant access to DNA Foundry team
:width: 80%
:align: center

```

Save edits to the settings by clicking "Done".

```{figure} ../_static/images/done.png
:alt: grant access to DNA Foundry team
:width: 50%
:align: center

```

→ [How to add a user or a Team as collaborator in your project](https://help.benchling.com/hc/en-us/articles/9684263074445-Set-project-permissions)

## Register samples directly in your Notebook Entry

In order to register samples to submit to DNA Foundry, you can follow a **Sub-template** created by LIMS support for this purpose. 

Follow this video to learn how to do it:

````{raw} html
<iframe width="560" height="315" src="https://www.youtube.com/embed/iEUbB_NAL1k?si=7SPdNXcdMwIMLhsO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
````

_Summary of the steps:_

1. Navigate to your experiment **Notebook Entry**

2. Insert the **sub-template** "Nanopore Sample Submission" in the Entry

→ You can choose between different samples storage options: **Plate**, **Box**, single **Vials**.

3. **Fill-in** the registration and inventory tables that appeared in your Notebook Entry with the required metadata.

4. **Copy** (Command+C / CTRL+C) the newly-registered **samples entities** from the last table



## Create a Workflow

In order to submit your newly-registered samples for analysis to the DNA Foundry team, you need to create a Workflow and attach the samples within it. The Workflow to submit samples to the DNA Foundry is labelled with "DNF".

Follow this video to learn how to do it:

````{raw} html
<iframe width="560" height="315" src="https://www.youtube.com/embed/lQ9xJghtMv4?si=dM0PppQa0VyCpNtq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
````

## VERY IMPORTANT!!

When creating a workflow, **paste all the samples in one single cell** in the "DNF Nanopore Samples" column (as showed in the screenshot downbelow, and in the video). If you have sample-level metadata, please add them in the previous step (when you are registering the  samples in your Notebook entry). 

```{figure} ../_static/images/important-samples-in-one-cell-nanopore.png
:alt: Paste samples in one cell
:width: 100%
:align: center

```

You can achieve it by using the "Paste special" button:

```{figure} ../_static/images/paste-special-nanopore.png
:alt: Use Paste Special to paste all samples in one cell
:width: 80%
:align: center

```

_Summary of the steps:_

1. **Create** a Workflow of the relevant type.

2. **Select "Table" format** for your Task table

```{figure} ../_static/images/table-format-in-workflow-nanopore.png
:alt: create a Workflow
:width: 90%
:align: center

```

3. **Paste** the samples entities in a **single** **DNF Nanopore Samples** column cell 

```{figure} ../_static/images/paste-special-nanopore.png
:alt: Use Paste Special to paste all samples in one cell
:width: 80%
:align: center

```

4. **Fill-in** the remaining metadata fields.

→ Remember to specify the correct **"Project number"** and to save the Workflow in the relevant **Project folder** (the video's Project number and Project folder are used as examples).

5. Click on **"Create"**. The analyst will receive an email and therefore will be informed about your submission. 


## List of available Workflows

This is the available list of Workflows (currently only one for the DNA Foundry Team):

```{figure} ../_static/images/dnf-workflows-list.png
:alt: create a Workflow
:width: 50%
:align: center

```

<br/><br/>

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).

