# (For analysts only) Execute DNF Workflow

```{admonition} ⚠️ *Important*
:class: my-custom-admonition

This guide is intended for Biosustain **DNA Foundry team** only.
``` 

🎯 This guide will show you how to **execute** the "DNF Workflow" submitted by researchers or DNA Foundry team members at Biosustain.
Follow **[this guide](/guides/nanopore_samples_submission.md)** if you need to **create** the workflow instead.

A **Benchling Workflow** contains:
- details of the **samples** to be analysed
- details of the **analysis** to be performed (in this case, only Nanopore sequencing is available)

## 📩 Check your inbox for new submissions

As an **Analyst**, **you will receive an email notification** once a new Workflow  is created (you will receive notifications only for the Workflow you are responsible for).

### Access the submitted Workflow

Click on the link provided in the email.
Example: 

```{figure} ../_static/images/access-workflow-dnf.png
:alt: access the workflow
:width: 90%
:align: center

```

## 📆 Update the Workflow status to "Planned"

 ```{admonition} ❗️
:class: my-custom-admonition

If you are the person who created the workflow, you can skip this step.
``` 

When you are about to start the analysis, **you can update the Workflow status** to "PLANNED" to let the researcher know you are on it. 


_We suggest to use the status "Planned" instead of "In progress" because this enables for a more straightforward execution of the workflow later-on._

To udpate the status, go the the **"Tasks" table**, click **"Edit"**, and edit the "**Status**" column. Now click **"Submit"** to save the edit.

```{figure} ../_static/images/edit-task-table-dnf.png
:alt: update the status of the workflow
:width: 80%
:align: center

```

### Execute the Workflow

When you are ready to register all relevant information about the analysis run (either before or after the analysis is done), you can click on the **"Execute"** blue icon.

```{figure} ../_static/images/execute-workflow-dnf.png
:alt: execute workflow
:width: 80%
:align: center

```

### Create new Execution Entry 

In the pop-up windown that showed up click "Execute" again, and a new Notebook Entry (from Template) will be automatically created. Follow the steps in the Notebook Entry to register the relevant information regarding the analysis run.


### Submit the Output table 

After adding the relevant information in the various tables of the Notebook Entry, you can fill in the Output table, for example adding the **link to the Output folder** where the data can be found and accessed.

```{figure} ../_static/images/submit-output-dnf.png
:alt: submit output
:width: 80%
:align: center

```

Submitting the Output table will **automatically change the status of the Workflow task to "Completed"**. 

**The submitter will now receive a notification** that the analyis is completed and the results ready to be accessed.
