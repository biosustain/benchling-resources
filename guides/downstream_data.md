# Register Downstream data - draft

 ```{admonition} ⚠️
:class: my-custom-admonition

This guide is intended for the **Pre-Pilot Plant team**. To be able to follow the steps in the guide, you need to be **added to the [Pre-Pilot Plant team](https://biosustain.benchling.com/teams/team_zsgxMbi3/projects)** in Benchling. 
``` 
<br/>

 ```{admonition} ⚙️
:class: my-custom-admonition

This guide is a draft. 
The showed implementation can only be found in **Benchling Test Environment**.
``` 

## Test the implementation

To test the implementation showed in the guide, access Benchling Test Environment:
<br/>

🔗 [https://dtubiosustaintest.benchling.com/](https://dtubiosustaintest.benchling.com/)

If you cannot access, we have to create a profile for you. [Contact us](/contact.md).

## 1. Create new Notebook entry (ELN) from Template

Create your new Notebook Entry starting from a Template:

```{figure} ../_static/images/create-eln-from-template-downstream1.png
:alt: create 
:width: 80%
:align: center
```

```{figure} ../_static/images/create-eln-from-template-downstream2.png
:alt: create 
:width: 100%
:align: center
```

## 2. Identify starting material 

The starting material could be a _Fermentatin Culture_ entity created by the Upstream team, or created by you (see Option 1 and Option 2 in the screenshot downbelow).

```{figure} ../_static/images/starting-material-downstream.png
:alt: Identify starting material 
:width: 100%
:align: center
```

_Note: If the starting material is not of type "Fermentation Culture", you can add your own registration table of type "Processed Material"_. (_Insert > Registration table > Schema "Processed Material"_)

## 3. Add first processing step 

Register your first processing step by adding a new Sub-Template:

☑️ Insert Sub-Template:

```{figure} ../_static/images/add-subtemplate-downstream1.png
:alt: Insert Sub-Template
:width: 50%
:align: center
```

☑️ Select the relevant step you need:
```{figure} ../_static/images/add-subtemplate-downstream2.png
:alt: Select step type
:width: 80%
:align: center
```

### Example: Filtration

☑️ Add starting material:

Add the Output of the previous step (in the case it is the Fermentation Culture) in the Lookup table called **"Input"** 


☑️ Create output material:

Create the output material by clicking on *"Submit"* in the Registration table **Output**.


☑️ Capture information about the processing steps:

Select or type all the needed parameters, including initial and final volume, and used equipment. 


```{admonition} ℹ️ Hidden columns (Concentration)
:class: my-custom-admonition

The columns **"Initial Concentration"** and **"Final Concentration"** are hidden. To add them to the table, right-click on any of the column and select "Insert column left" or "Insert column right".
``` 
<br/>

```{figure} ../_static/images/example-step-filtration-downstream.png
:alt: Filtration step
:width: 100%
:align: center
```

### Making edits to the step

#### ✏️ Update Dropdowns

If you notice that one of the dropdowns in the "Step" table (in this case the "Filtration" table) is missing a value, you can add it yourself.

1. Go to the [Dropdowns page](https://biosustain.benchling.com/biosustain/registries/src_1MhfzKi0/dropdowns/) in Benchling
2. Type the *Step name* in the search bar, for example "*Filtration*"
3. Find the relevant dropdown that you need to update
4. Add option to the dropdown.

```{figure} ../_static/images/downstream-add-option-to-dropdown.gif
:width: 50%
:align: center

```
#### ✏️ Create new equipment

If you need to add a new equipment in Benchling, follow the instructions contained in this [Notebook Entry](https://biosustain.benchling.com/biosustain/f/lib_N0MVgvr6oL-downstream-data-capture-ppp/etr_XoztnU2Sj6-registration-of-new-equipment/edit).

To check the full list of existing Equipment, following this link:
- [List of existing equipment](https://biosustain.benchling.com/search?filter=types%3AIS_ONE_OF%3Abasic_folder_item%3Bschema%3AIS_ONE_OF%3Ats_IV0dk9kVUH%3BarchivePurposes%3AIS_ONE_OF%3ANOT_ARCHIVED%3BisAssociatedWithUnsubmittedRequestV2Submission%3AIS_FALSE%3BProcessesIsSystemDataFilter%3AIS_FALSE&offset=0&limit=100&sorts=name%3A0&q=&v=2)


#### ✏️ Create new step


If you need to capture a new processing step that is not covered by the current implementation, [contact LIMS Support](/contact.md). Please provide the following information:

- Process name (e.g., Filtration)
- Different types of process (e.g., Microfiltration, Ultrafiltration)
- Specific parameters that you need to capture in this process (e.g., Membrane type, Temperature (C), ph, Pressure (bar))

To check the full list of existing steps and related parameters, following this link:
- [List of existing steps](https://biosustain.benchling.com/search?q=step)

## 4. Add next processing step

New processing steps can be added by adding additional Sub-templates:

```{figure} ../_static/images/add-subtemplate-downstream2.png
:alt: Add next step 
:width: 100%
:align: center
```


## Dashboard

You will find the links to the available dashboards at the beginning of the Notebook entry.

### Example: 

In the _Fermentation Culture Processing Dashboard_ add the IDs of the Fermentation Cultures you want to compare the yield or the process for:

```{figure} ../_static/images/comparison-dashboard-downstream1.png
:alt: Dashboard 
:width: 90%
:align: center
```

```{figure} ../_static/images/comparison-dashboard-downstream2.png
:alt: Dashboard 
:width: 90%
:align: center
```

To change the selected Fermentation Cultures, click on the _[...] icon > "Edit parameters"_.


```{figure} ../_static/images/edit-parameters-downstream.png
:alt: Edit parameters 
:width: 90%
:align: center
```


<br/><br/>
If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).
