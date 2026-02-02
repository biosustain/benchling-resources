# Submit samples for analysis to Pre-Pilot-Plant (PPP)

Benchling has replaced one of its modules (**“Requests”**) with another new module (**“Workflow”**). To discover how to submit samples for analysis to the Pre-Pilot-Plant (PPP) team using Workflows, follow this guide. 

## Grant access to the PPP team to your Project
Add _Pre-Pilot Plant (PPP) Translational_ Benchling Team to the list of collaborators in your Project to enable the analysts to access the samples you are going to register. 

1. Navigate to your Benchling **Project settings** ⚙️

2. Add the _Pre-Pilot Plant (PPP) Translational_ Benchling Team to the list of collaborators (with **"WRITE"** access) 


```{figure} ../_static/images/grant-ppp-access-to-project.png
:alt: grant access to PPP team
:width: 80%
:align: center

```

Save edits to the settings by clicking "Done".

```{figure} ../_static/images/done.png
:alt: grant access to PPP team
:width: 50%
:align: center

```

→ [How to add a user or a Team as collaborator in your project](https://help.benchling.com/hc/en-us/articles/9684263074445-Set-project-permissions)

## Register samples directly in your Notebook Entry

In order to register samples to submit to PPP, you can follow a **Sub-template** created by LIMS support for this purpose. 

Follow this video to learn how to do it:

````{raw} html
<iframe width="560" height="315" src="https://www.youtube.com/embed/It1ynr57418?si=HFiC2BF2bXy3BCZe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
````

_Summary of the steps:_

1. Navigate to your experiment **Notebook Entry**

2. Insert the **sub-template** "PPP Sample Submission" in the Entry

    → You can choose between different samples storage options: **Plate**, **Box**, single **Vials**.

3. **Fill-in** the registration and inventory tables that appeared in your Notebook Entry with the required metadata.

    ```{admonition} *Note*
    :class: my-custom-admonition

    When moving samples in a Box or a Plate, please do so **row-wise** (A1, A2, A3...) as showed in the video.

    ```
4. **Copy** (Command+C / CTRL+C) the newly-registered **samples entities** from the last table

## Create a Workflow

In order to submit your newly-registered samples for analysis to the PPP team, you need to create a Workflow and attach the samples within it. 

 ```{admonition} *Note*
:class: my-custom-admonition

In order to submit your newly-registered samples for analysis to the PPP team, you need to create a Workflow and attach the samples within it. The Workflow to submit samples to the PPP team is labelled with "PPP".

```

Follow this video to learn how to do it:

````{raw} html
<iframe width="560" height="315" src="https://www.youtube.com/embed/HS5id6d6lmo?si=W3Zufs0Rj6rcJJUm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
````

## VERY IMPORTANT!!

When creating a workflow, **paste all the samples in one single cell** in the "PPP Samples" column (as showed in the screenshot downbelow, and in the video). If you have sample-level metadata, please add them in the previous step (when you are registering the  samples in your Notebook entry). 

```{figure} ../_static/images/important-samples-in-one-cell-ppp.png
:alt: Paste samples in one cell
:width: 100%
:align: center

```

You can achieve it by using the "Paste special" button:

```{figure} ../_static/images/paste-special-ppp.png
:alt: Use Paste Special to paste all samples in one cell
:width: 80%
:align: center

```

_Summary of the steps:_

1. **Create** a Workflow of the relevant type, based on the analysis your are interested in.

2. **Select "Table" format** for your Task table

```{figure} ../_static/images/table-format-in-workflow-ppp.png
:alt: create a Workflow
:width: 90%
:align: center

```

3. **Paste** the samples entities in a **single** **PPP Samples** column cell 

```{figure} ../_static/images/paste-special-ppp.png
:alt: Use Paste Special to paste all samples in one cell
:width: 80%
:align: center

```

4. **Fill-in** the remaining metadata fields.

→ Remember to specify the correct **"Project number"** and to save the Workflow in the relevant **Project folder** (the video's Project number and Project folder are used as examples).

5. Click on **"Create"**. The analyst will receive an email and therefore will be informed about your submission. 

## List of available Workflows

This is the available list of Workflows (currently only one for the PPP Team):

```{figure} ../_static/images/ppp-workflows-list.png
:alt: create a Workflow
:width: 50%
:align: center

```

<br/><br/>

If you have any question, don’t hesitate to contact us at [lims_support@bright.dtu.dk](mailto:lims_support@bright.dtu.dk).
