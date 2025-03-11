# Register media

 🎯 This guide will show you how to:
- **Register media** in Benchling with the Medium Recipe.
- **Track individual batches of media** you prepare for your experiments with Medium Batch.
- Leverage mixture prep tables to facilitate your media preparations.
- Build your library of media recipes.

## Overview of media schemas

Benchling has two schemas for media:
- **Medium Recipe** is the main schema to register your media.
- **Medium Batch** allows you to register individual preparations of a Medium Recipe.

```{figure} ../_static/images/media-guide-1.jpg
:alt: Demonstrates layers of annotation that plate maps can have
:width: 100%
:align: center
```

## How to register Medium Recipe entities

Medium Recipes are the base schema for your media in Benchling. You can register them in two different ways.

```{figure} ../_static/images/media-guide-2.png
:alt: Demonstrates layers of annotation that plate maps can have
:width: 70%
:align: center
```

- **Create a Medium Recipe from scratch:** define the medium composition (ingredients and their concentrations) from a blank starting point.
- **Create a Medium Recipe based on another Medium Recipe:** define the medium composition (ingredients and their concentrations) having a pre-existing Medium Recipe composition as starting point.

See how to:

### Create a Medium Recipe from scratch

````{raw} html
<div style="text-align: center;">
<iframe
    width="560" height="315" src="https://www.youtube.com/embed/DDK1mbwI9_w?si=_xI3cQtm3-a8s_hq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>
</div>
````

***Summary of the steps:***

**Step 1: Create a Medium Recipe entity.**
```
Benchling Navigation Bar: "Create (+)" > "Mixture" > "Medium Recipe"
```

**Step 2: Add the medium composition: select the ingredients and their concentrations.**

> Select the appropriate ingredient entities to represent the components used for the preparation of the mixture. For example:
> - Indicate a specific product with a **Commercial Material** entity (from orders).
> - More generally reference a chemical with a **Chemical Compound** entity (includes chemical formula).
> - Indicate a pre-prepared solution with **another Medium Recipe**.
>
> Pay extra attention to the concentration values **and units** for the ingredients in your Medium Recipes. Mixing up units can be a small mistake with big consequences.


**Step 3: Write recipe instructions.**

> Use the Instructions free text module to describe the preparation of the medium and its storage.

**Step 4: Fill out relevant schema fields, or add your own in Custom Fields.**

**Step 5: Add aliases.**

> Use aliases to indicate other names the medium might be know as. This could even be, for example, an internal ID for your media library. You can then reach you entity through any of the aliases when searching in Benchling.

**Step 6: *Register!***

### Create a Medium Recipe from another Medium Recipe

The process follows the same steps as **Create a Medium Recipe from scratch**, with the following changes:

**Step 1: Create a new Medium Recipe entity and *indicate the parental Medium Recipe.***

> Link the Medium Recipe that your new Medium Recipe will be based on in the 'Derived from' field of the pop-up window. 

```{figure} ../_static/images/media-guide-3.png
:alt: Demonstrates layers of annotation that plate maps can have
:width: 70%
:align: center
```

**Step 2: *Modify the composition of the new Medium Recipe.*** 

> The new Medium Recipe inherits the composition of the parental Medium Recipe. You should then apply the desired  modifications: add/remove ingredients, or change concentrations.  


## How to register Medium Batch entities
The Medium Batch schema allows you to manage individual preparations of Medium Recipes. 

```{figure} ../_static/images/media-guide-4.png
:alt: Demonstrates layers of annotation that plate maps can have
:width: 50%
:align: center
```

You may find this schema useful for the following reasons:
- **Leverage mixture prep tables** - a great tool to facilitate media prep and its documention in your ELN.
- **Track the batches of medium used in experiments** - link individual media preparations to your experiments, and control it as a variable.
- **Keep inventory** - Medium Batches can be added into Benchling Inventory.

### Create a Medium Batch from a Medium Recipe using a mixture prep table

````{raw} html
<iframe
    width="560" height="315" src="https://www.youtube.com/embed/S4mX3Mb9esg?si=pMgCXQIuN_xdO2Di" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>
````

***Summary of the steps:***

**Step 1: Insert a mixture prep table into your ELN entry.**
```
In entry: "Insert" > "Mixture prep table"
```
> Keep Name and registry ID settings as "Generate new registry IDs, and replace name according to name template" the name for your Medium Batch following **naming convention**: *(Medium Recipe name)*-*(number)*.

**Step 2: Indicate the Medium Recipe that your Medium Batch is following.**

> The mixture prep table will update the composition of your Medium Prep based on that defined in the Medium Recipe. By default, the composition will be presented as amount of each ingredient per 1 L of medium.

**Step 3: Adjust the target volume of medium you are preparing.**

> The mixture prep table will automatically calculate the actual amount of each ingredient for the total volume of medium you specify.

**Step 4: Paste the recipe instructions into the entry.**

> You can paste the instructions from Medium Recipe detailing how to prepare the medium with a click.

```
Mixture prep table top bar: "Insert parent instruction into entry"
```

**Step 5: Add details about the ingredients specific to your preparation.**

> These details could be the actual measured amounts of ingredient, or other notes you want to specify about the ingredients.

**Step 6: Fill out relevant schema fields.**

**Step 7: *Submit!***


## Tips

### Use Medium Recipe entities as ingredients
The preparation of medium may often require that some solutions are pre-prepared - these could be intermediate solutions that are mixed to compose the final medium, or supplements such as antibiotic stock solutions.

```{figure} ../_static/images/media-guide-5.png
:alt: Demonstrates layers of annotation that plate maps can have
:width: 80%
:align: center
```
To represent this laboratory workflow and document the recipes for both your solutions and media in Benchling, we recommend **creating Medium Recipe entities for those pre-prepared solutions, then using them as ingredients for your Medium Recipes**.


### Build your media library

Having a library of Medium Recipes for your project may help you document your experiments as you develop your work, and facilitate collaboration. A way to approach it is:

- Create a specific folder within your project to store Medium Recipes.
- Create a subfolder for your intermediate solutions recipes.
- Decide on a naming convention for the Medium Recipes and use it consistently.

### Bulk import Medium Recipes from a spreadsheet

If you are creating multiple Medium Recipes at once, bulk import of Medium Recipe composition from a spreadsheet may be the best option. Learn how to do it with Benchling guide [Import Mixture Ingredients in Bulk](https://help.benchling.com/hc/en-us/articles/9684226244621-Import-mixture-ingredients-in-bulk).


If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).
