# Register media

 🎯 This guide will show you how to:
- **Register media** in Benchling with **Medium Recipe**, and build your library of media integrated into the Benchling workflow.
- **Keep track of individual batches** of media you prepare for your experiments with **Medium Batch**, and leverage mixture prep tables to facilitate your media preparations.

## Overview of media schemas

Benchling has two schemas for media:
- **Medium Recipe** is the main schema to register your media.
- **Medium Batch** allows you to register individual preparations of a Medium Recipe.

```{figure} ../_static/images/media-guide-1.jpg
:alt: Demonstrates layers of annotation that plate maps can have
:width: 100%
:align: center
```

## Create Medium Recipe and Medium Batch entities
```{figure} ../_static/images/media-guide-2.jpg
:alt: Demonstrates layers of annotation that plate maps can have
:width: 100%
:align: center
```

### (1) Create a Medium Recipe from scratch

````{raw} html
<div style="text-align: center;">
<iframe
    width="560" height="315" src="https://www.youtube.com/embed/DDK1mbwI9_w?si=_xI3cQtm3-a8s_hq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>
</div>
````


*Steps:*

**1. Create a Medium Recipe entity**, assign name and folder.
```
> Benchling Navigation Bar: "Create (+)" > "Mixture" > "Medium Recipe"
```

**2. Add the medium composition**: select the ingredients and their concentrations. 

> Select the appropriate ingredient entities to represent the components used for the preparation of the mixture. For example:
> - Indicate a specific product with a **Commercial Material** entity (from orders).
> - More generally reference a chemical with a **Chemical Compound** entity (includes chemical formula).
> - Indicate a pre-prepared solution with **another Medium Recipe**.
>
> Make sure the concentration values and units are correct.


**3. Write recipe instructions**: describe preparation of the media and other important notes.

**4. Fill out relevant schema fields**, or add your own in Custom Fields.

**5. Add an alias**: e.g., an ID for your media library.

**6. *Register!***

### 2. Create a Medium Recipe from another Medium Recipe
*Steps:*

**1. Create a Medium Recipe entity, and *link parent Medium Recipe in 'Derived from' field***, assign name and folder.

        Benchling Navigation Bar > "Create (+)" > "Mixture" > "Medium Recipe"

```{note}
Alternative: Navigate to *MEDIUM RECIPE* tab from pre-existing Medium Recipe and create a Medium Recipe entity. New Medium Recipe will automatically be 'Derived from' parent Medium Recipe.
```

**2. Modify the composition of the new Medium Recipe**: add/remove ingredients, or change concentrations.  

**3. Write recipe instructions**: describe preparation of the media and other important notes.

**4. Fill out relevant schema fields**, of add your own in Custom Fields.

**5. Add an alias**: e.g., an ID for your media library.

**6. *Register!***

### 3. Create a Medium Batch from a Medium Recipe

````{raw} html
<iframe
    width="560" height="315" src="https://www.youtube.com/embed/S4mX3Mb9esg?si=pMgCXQIuN_xdO2Di" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>
````

When preparing media for your experiments, we recommend **mixture prep tables** to:
- document media preparation details within your ELN entries
- automatically calculate amounts of each ingredient depending on Medium Batch volume
- add preparation instructions from the recipe into ELN 

*Steps:*
1. Insert a mixture prep table into your ELN entry.
2. Indicate the Medium Recipe that your Medium Batch is following.
3. Adjust the total amount of media you are preparing.
4. Fill out relevant schema fields.
5. Submit!


## Extra tips

- Use Medium Recipe entities as ingredients

- Build your library of media

```{tip}
If your medium is composed of a mixture of pre-prepared solutions, create Medium Recipe entities for those solutions beforehand. This way you have detailed recipes for the intermediate solutions, and you can use them as ingredients for your media in Benchling as you do in the laboratory. 
Figure
```

- Link to Import mixture ingredients in bulk 



If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).
