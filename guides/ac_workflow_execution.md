# (For analysts only) Execute analysis submissions by researchers

 ```{admonition} *Important*
:class: my-custom-admonition

This guide is intended for Biosustain **Analytics team** only.
``` 
🎯 This guide will show you how to execute analysis submissions created by researchers at Biosustain.

**Researchers uses Workflows to request for samples to be analyzed in-house**. The **output** of this request is a **Benchling Workflow** that contains:
- details of the **samples** to be analysed
- details of the **analysis** to be performed

Researchers can **choose from the following Workflows**:

- GC-MS analysis
- Proteomics
- Targeted Metabolomics
- Untargeted Metabolomics

## 📩 Check your inbox for new submission by researchers

As an **Analyst**, **you will receive an email notification** once a new analysis submission has been created by a researcher (you will receive notifications only if the submission is relative to the analysis type you are responsible for).

### Access the submitted Workflow

Click on the link provided in the email.
Example: 

```{figure} ../_static/images/access-workflow.png
:alt: access the workflow
:width: 80%
:align: center

```

## 📄 Download samples list 

In order to **download the full list of samples and the relative details** (including sample position e.g., A1, A2,...), access the Sample List dashboard and download the list as .csv file.

### **Copy the Workflow ID** 

**Copy the Workflow ID** from the Task table (in the following example image, the Workflow ID is  **GCMS8-T1**)

```{figure} ../_static/images/copy-workflow-id.png
:alt: copy workflow ID
:width: 100%
:align: center

```

### Access the Sample List dashboard

**Click on the link** included under the "Instruction" field to access the Sample List Dashboard:

```{figure} ../_static/images/download-samples-list-1.png
:alt: example of a workflow
:width: 100%
:align: center

```

### Paste the Workflow ID

**Paste the Workflow ID** to configure the workflow_task_id parameter, click the "_more options_" icon [...] and select "Download as .csv:

```{figure} ../_static/images/download-samples-list-2.png
:alt: download .csv file
:width: 100%
:align: center

```

## 📆 Update the Workflow status to "Planned"

When you are about to start the analysis, **you can update the Workflow status** to "PLANNED" to let the researcher know you are on it.

_We suggest to use the status "planned" instead of "in progress" because this enables for a more straightforward execution of the workflow later-on._

To udpate the status, go the the **"Tasks" table** (where the details of the submissions are), click **"Edit"**, and edit the "**Status**" column. Now click **"Submit"** to save the edit.

In the same table, you can also set yourself as "**Assignee**" of the analysis, and set a date for when the results will be available to the researcher by editing the "**Scheduled on**" column.

```{figure} ../_static/images/edit-task-table.png
:alt: update the status of the workflow
:width: 100%
:align: center

```

## Attach the results

When you are done with the analysis and you produced results, you are ready to execute the Workflow.

### Execute the Workflow

To execute the workflow, click on the **"Execute"** blue icon.

```{figure} ../_static/images/execute-workflow.png
:alt: execute workflow
:width: 100%
:align: center

```

### Add the file as attachment

In the pop-up windown that showed up after clicking "Execute", scroll directly to the Output table at the botton, and attach the result file by double clicking on the **"Result (Attachment)"** column.

After attaching the file, click on **"Continue"**.


```{figure} ../_static/images/attach-results.png
:alt: attach result file
:width: 100%
:align: center

```

### Submit

At this stage, you will be able to review all the details of the Workflows (Task + Output tables) and see if everything is correct.

If everything looks correct, click on **"Submit"**.


```{figure} ../_static/images/submit-execution.png
:alt: execute workflow
:width: 100%
:align: center

```

**The researcher will now receive a notification that the analyis is completed and the results are ready to be accessed.**


## Troubleshooting

```{dropdown} The "Execute" icon is not clickable.
Check the status of the Workflow. If the status is different from "pending" or "planned", you will not be able to execute the Workflow. You will need to manually "Edit" the status of the Workflow in the "Tasks" table, and manually "Edit" the "Output" table and attaching the result file. Remember to click "Submit" to save the edits.
```

```{dropdown} Raw data
The implementation doesn't currently allow to attach raw data. Only use the "Result (Attachment)" for pre-processed data. You can send raw data by email to the researcher.
```

<br/><br/>

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).