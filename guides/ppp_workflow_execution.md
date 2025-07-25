# Execute PPP Workflow


```{admonition} ⚠️
:class: my-custom-admonition

This guide is intended for the **Pre-Pilot Plant team**.
``` 

🎯 This guide will show you how to execute Workflows submitted by researchers (or yourself) at Biosustain.
Follow **[this guide](/guides/ppp_samples_submission.md)** if you need to **create** a Workflow instead.

## What is a Benchling Workflow?

A **Benchling Workflow** contains:
- details of the **samples** to be analysed
- details of the **analysis** to be performed
- details of who submitted the Workflow

The submitter can **choose between [different assays](https://biosustain.benchling.com/biosustain/registries/src_1MhfzKi0/dropdowns/sfs_mFMjVMtw)**. If you want a new assay to be added to the options, [contact LIMS support](/contact.md).

## 📩 Check your inbox for new submission

As an **Analyst**, **you will receive an email notification** once a new Workflow  is created by a researcher (you will receive notifications only for the Workflow you are responsible for).

### Access the submitted Workflow

Click on the link provided in the email.
Example: 

```{figure} ../_static/images/access-workflow-ppp.png
:alt: access the workflow
:width: 80%
:align: center

```

## *Before the analysis*

## 📄 Download samples list 

If you need to **download the full list of samples and the relative details** (including sample position e.g., A1, A2,...), access the Sample List dashboard and download the list as .csv file.



### **Copy the Workflow ID** 

**Copy the Workflow ID** from the Task table (in the following example image, the Workflow ID is  **QUANT776-T1**)

```{figure} ../_static/images/copy-workflow-id-ppp.png
:alt: copy workflow ID
:width: 100%
:align: center

```

### Access the Sample List dashboard

**Click on the link** included under the "Instruction" field to access the Sample List Dashboard:

```{figure} ../_static/images/download-samples-list-1-ppp.png
:alt: example of a workflow
:width: 100%
:align: center

```

### Paste the Workflow ID

**Paste the Workflow ID** to configure the workflow_task_id parameter, click the "_more options_" icon [...] and select "Download as .csv:

```{figure} ../_static/images/download-samples-list-2-ppp.png
:alt: download .csv file
:width: 85%
:align: center

```

## 📆 Update the Workflow status to "Planned"

When you are about to start the analysis, **you can update the Workflow status** to "PLANNED" to let the researcher know you are on it.

_We suggest to use the status "Planned" instead of "In progress" because this enables for a more straightforward execution of the workflow later-on._

To udpate the status, go the the **"Tasks" table** (where the details of the submissions are), click **"Edit"**, and edit the "**Status**" column. Now click **"Submit"** to save the edit.


```{figure} ../_static/images/edit-task-table-ppp.png
:alt: update the status of the workflow
:width: 100%
:align: center

```

## *After the analysis*

### Execute the Workflow

When you are done with the analysis and you produced results, you are ready to execute the Workflow.

To execute the workflow, click on the **"Execute"** blue icon.

```{figure} ../_static/images/execute-workflow-ppp.png
:alt: execute workflow
:width: 80%
:align: center

```

### Create new Execution Entry 

In the pop-up windown that showed up click "Execute" again, and a new Notebook Entry (from Template) will be automatically created. Follow the steps in the Notebook Entry to upload the data using LIMS extension. 


### Send the Entry for Review

After adding the data using LIMS extension _"Analytical Chemistry Compound Quantification"_, you can finally send the Notebook Entry for Review. This will enable the data to be downloaded in the LIMS exension _"Fermentation reports > Export"_.

```{figure} ../_static/images/send-eln-for-review.png
:alt: execute workflow
:width: 80%
:align: center

```

Accepting the Review will **automatically change the status of the Workflow task to "Completed"**. 

**The submitter will now receive a notification** that the analyis is completed and the results are ready to be downloaded in Benchling (or LIMS extensions _"Fermentation reports > Export"_).


## Troubleshooting

```{dropdown} Why I cannot accept the Notebook Entry during the review process?
In order to being able to accept the Notebook Entry in the review process, you need to have the status of "Auditor" in the Project folder in which the Notebook Entry is saved. Learn how to add auditors in the project [here](https://help.benchling.com/hc/en-us/articles/9684260674189-Add-auditors-for-Notebook-reviews).
```

<br/><br/>

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).