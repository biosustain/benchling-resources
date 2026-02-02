# Register Downstream data

 ```{admonition} ⚠️
:class: my-custom-admonition

This guide is intended for the **Pre-Pilot Plant team**. To be able to follow the steps in the guide, you need to be **added to the [Pre-Pilot Plant team](https://bright.benchling.com/teams/team_zsgxMbi3/projects)** in Benchling. 
``` 

## 1. Create new Notebook entry (ELN) from Template

Create your new Notebook Entry starting from a Template:

```{figure} ../_static/images/downstream-entry-from-template.png
:alt: create 
:width: 90%
:align: center
```

Search for the template collection "PPP Templates" and select template "PPP Downstream":

```{figure} ../_static/images/downstream-entry-from-template2.png
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
:width: 80%
:align: center
```

☑️ Select the relevant step you need:
```{figure} ../_static/images/downstream-subtemplate-selection.png
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


```{admonition} ℹ️ Hidden column (Concentration)
:class: my-custom-admonition

The column **"Concentration (mg/L)"** is hidden. To add it to the table, right-click on any of the column and select "Insert column left" or "Insert column right".
``` 
<br/>

```{figure} ../_static/images/example-step-filtration-downstream.png
:alt: Filtration step
:width: 100%
:align: center
```
## 4. Add next processing step

New processing steps can be added by adding additional Sub-templates:

```{figure} ../_static/images/downstream-subtemplate-selection.png
:alt: Add next step 
:width: 100%
:align: center
``` 

## Edit the implementation

Any changes to the implementation requires you to be part of the [Pre-Pilot Plant Benchling team](https://bright.benchling.com/teams/team_zsgxMbi3/projects). 

### ✏️ Update Dropdowns

If you notice that one of the dropdowns in the "Step" table (in this case the "Filtration" table) is missing a value, you can add it yourself.

1. Go to the [Dropdowns page](https://bright.benchling.com/biosustain/registries/src_1MhfzKi0/dropdowns/) in Benchling
2. Type the *Step name* in the search bar, for example "*Filtration*"
3. Find the relevant dropdown that you need to update
4. Add option to the dropdown.

```{figure} ../_static/images/downstream-add-option-to-dropdown.gif
:width: 50%
:align: center

```
### ✏️ Create new equipment

If you need to add a new equipment in Benchling, follow the instructions contained in this [Notebook Entry](https://bright.benchling.com/biosustain/f/lib_N0MVgvr6oL-downstream-data-capture-ppp/etr_XoztnU2Sj6-registration-of-new-equipment/edit).

To check the full list of existing Equipment, following this link:
- [List of existing equipment](https://bright.benchling.com/search?filter=types%3AIS_ONE_OF%3Abasic_folder_item%3Bschema%3AIS_ONE_OF%3Ats_IV0dk9kVUH%3BarchivePurposes%3AIS_ONE_OF%3ANOT_ARCHIVED%3BisAssociatedWithUnsubmittedRequestV2Submission%3AIS_FALSE%3BProcessesIsSystemDataFilter%3AIS_FALSE&offset=0&limit=100&sorts=name%3A0&q=&v=2)

### ✏️ Add new parameters to an existing step

If you need to capture a new parameters in a specific step:

1. Search for the entity schema (in this case a Step") of interest in the [Benchling Settings dedicated to Entity Schemas](https://bright.benchling.com/biosustain/registries/src_1MhfzKi0/tag-schemas/)

2. Click on the entity schema to enter the specific settings

3. Scroll down to the "entity fields" table

4. Add a new metadata field by clicking the "+" icon:

```{figure} ../_static/images/downstream-add-new-field.png
:width: 90%
:align: center
```
5. Fill-in the different columns:
    - "Entity field": Give the new parameter a name. Remember to specify the unit in parenthesis (for example: _Temperature (ºC)_)
    - "System name": this will automatically be created
    - "Required": mark if this field is mandatory to fill-in or not
    - "Multi-select": mark if multiple options can be selected for this field
    - "Parent link": you can skip this column
    - "Definition": select which type of field this is (numerical, text, dropdown, entity link, ...)
        - If it is a dropdown, remember to create a dropdown beforehand
        - If it is an entity link, select the specific entity type (strain, chemical coumpond, ...)

If you need help in making this changes, you can always [contact LIMS Support](/contact.md).


### ✏️ Create new step

If you need to capture a new processing step that is not covered by the current implementation, [contact LIMS Support](/contact.md). Please provide the following information:

- Process name (e.g., Filtration)
- Different types of process (e.g., Microfiltration, Ultrafiltration)
- Specific parameters that you need to capture in this process (e.g., Membrane type, Temperature (C), ph, Pressure (bar)). Consider that the following parameters are going to automatically be added to the new processing step, as these are in common across all the steps:

```{figure} ../_static/images/downstream-fieldset-step.png
:alt: Shared parameters across all steps
:width: 90%
:align: center
```


To check the full list of existing steps and related parameters, following this link:
- [List of existing steps](https://bright.benchling.com/search?q=step)

### ✏️ Create a downstream processing template

If you want to create a template with pre-defined processing steps (for example, to be used in the context of a specific project), you can create a duplicate template from the base template ("_PPP Downstream_") and add all needed processing steps. (Consider that if you already have done this, you can also select another template created for another project). 

1. Go to feature settings > Template collections
 
```{figure} ../_static/images/ downstream-template-collection-menu.png
:alt: 
:width: 90%
:align: center
```

2. Type "PPP" to search for the Template collection of interest, and search for the Template you want to duplicate. If you want a empty template, select "PPP Downstream" (the basic template showed in Step 1 of the guide).

```{figure} ../_static/images/downstream-base-template.png
:alt: 
:width: 100%
:align: center
```

3. Go in the Template, click to the "History" icon, and then select "Dulicate from Version", as showed down below:

```{figure} ../_static/images/downstream-duplicate-from-version.png
:alt: 
:width: 100%
:align: center
```

4. Add all the Steps that you want to add for this template, and then publish the draft.

```{figure} ../_static/images/downstream-publish-template.png
:alt: 
:width: 100%
:align: center
```

5. If you need to edit the published draft, just select "Create New Draft":

```{figure} ../_static/images/downstream-create-new-draft.png
:alt: 
:width: 100%
:align: center
```

6. To start capturing downstream data with this new template, select it when creating a new Notebook Entry (follow step 1. of the guide -"Create new Notebook entry (ELN) from Template"- and select your new template). 

## Dashboards

Here is the list of existing dashboards:
- [Fermentation Culture Processing Dashboard](https://bright.benchling.com/analytics/dashboards/axdash_tciiECE1Jb-downstream-fermentation-culture-processing-dashboard)

## Compare Fermentation Culture processing and yield

In the _Fermentation Culture Processing Dashboard_, add the IDs of the Fermentation Cultures for which you want to compare the yield and the process:

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
If you have any question, don’t hesitate to contact us at [lims_support@bright.dtu.dk](mailto:lims_support@bright.dtu.dk).
