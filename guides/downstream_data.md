# Register Downstream data - draft

 ```{admonition} ⚠️
:class: my-custom-admonition

This guide is intended for the **Pre-Pilot Plant team**.
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

Insert Sub-Template:

```{figure} ../_static/images/add-subtemplate-downstream1.png
:alt: Insert Sub-Template
:width: 50%
:align: center
```

Select the relevant step you need:
```{figure} ../_static/images/add-subtemplate-downstream2.png
:alt: Select step type
:width: 80%
:align: center
```

### Example: Filtration

Fill in the Input, Output and Step table to register the necessary step metadata. 

```{figure} ../_static/images/example-step-filtration-downstream.png
:alt: Filtration step
:width: 100%
:align: center
```

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


## Implementation status:
New _Step "types"_ (and relevant equipment and parameters) needs to be identified.
<br/><br/>

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).