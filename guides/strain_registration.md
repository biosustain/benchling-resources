# Register strains in Benchling

> Author: Mía López Portillo Ontiveros

## Overview
This article will teach you how to register a strain in Benchling from your Notebook. 

```{note}
Registering your strains in Benchling will make it easier for you to **keep track of their lineage**, links to other entities such as plasmids and parent strains, and their **storage locations** at Biosustain.
```

## Pre-requisites
Before registering your strains, register relevant linked entities such as the **organism** (i.e. *Escherichia coli*, *Pichia pastoris*, etc.), the **parent strain**, **plasmids**, or a specific **medium**. In order to link your strains to these other entities, they must be registered beforehand. 

```{note}
Organisms and Media must be stored in the **Biosustain Common Inventory** project in Benchling (to avoid needing to register the same Organism or Medium multiple times).
```

### About registration fields
|Field         |Definition   |
|--------------|-------------|
|Host strain   |A well-characterized microbial strain, like *E. coli BL21*, used as the baseline for genetic manipulation or protein expression.   |
|Parent strain |A genetically modified derivative of the host strain that serves as the starting point for further modifications.   |

## How to register a strain

```{note}
Each step is shown in the video down below. 
```

1. **Open your ELN (or create a new ELN page)**

    Registering Strains directly in the ELN is the recommended way to register strains. 
    You can create a specific Notebook related to strain registration, or you can add registration tables in your experimental ELNs as you go. 

2. **Insert a strain registration table**

    *“Insert” > “Registration table”*

3. **Fill in the information**

    There are some mandatory fields, the rest are optional. You can fill all the fields that are relevant to you. Fields that link to other entities require the exact entity name.  

    ```{note}
    You can drag down cells to auto-fill names if you are following a numerical sequence.
    ```
4. **Click on “Submit”!**

    If there is any issue with the registration, the side of the table will be red, and you will get an error message. 

    If there are no validation errors, your strains will now be registered!


````{raw} html
<div style="text-align: center;">
   <iframe 
      width="560" 
      height="315" 
      src="https://www.youtube.com/embed/_4SFBM0M1iA?si=CfAimXGJYZkgAKo1?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
   </iframe>
</div>
````


## How to store a strain

````{figure} ../_static/images/store-a-strain-v2.png
:alt: Strain-storage
:width: 90%
:align: center

````

```{note}
Each step is shown in the video down below. 
```
1. **Insert the “Strain storage” sub-template**

    *Insert > Sub-Template > LIMS Support > Strain Storage*

2. **Fill-in and submit each registration table** 

    *Three tables are needed to successfully store your strain(s):*

    a. Strain batch registration

    Allows you to create entities representing a physical batch of a strain. You can have multiple batches for a single strain.

    b. Box creation

    Allows you to generate a new, empty box in your preferred location (e.g., a Freezer)

    c. Container creation

    Helps you create vials for the samples and lets you store them in the box. 

````{raw} html
<div style="text-align: center;">
   <iframe 
      width="560" 
      height="315" 
      src="https://www.youtube.com/embed/-MP_b3G6ULg?si=yfGJ5ZpS7JKkViui?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
   </iframe>
</div>
````



## Can I do this from a spreadsheet?
Yes, you can easily register strains by uploading a spreadsheet onto a strain registration table. Your spreadsheet must have columns corresponding to some or all of the required fields. 

```{important}
**You can use the following template for strain registration:** {download}`Strain_Template_YourName.xlsx <../_static/files/Strain_Template_YourName.xlsx>`.
* Red fields are mandatory
* Blue fields refer to registered entities
```

```{caution}
Benchling will try to match the names in blue fields to entities in the registry. If multiple entities have the same name, you will get a **validation error**. 

It is recommended to use **registry IDs** (which are unique) instead of entity names to prevent this issue.
```

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


## Tips and tricks

You can register from a table multiple times, without duplicating registries – only the changes and additions are uploaded! You can use this to update registered entities or add new ones from the same table.   
