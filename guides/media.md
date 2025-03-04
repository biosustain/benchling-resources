# Register media

 🎯 This guide will show you how to **register media in Benchling** and guide you on how to:
 - Build your library of media by creating Medium Recipes from scratch, or from related Medium Recipe entities.
 - Create Medium Batch from a Medium Recipe and leverage mixture prep tables to facilitate your media preparations.

## Overview of media schemas

Benchling has two schemas to register media: **Medium Recipe** and **Medium Batch**.

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

1. Create a Medium Recipe entity, assign name and folder.

        Benchling Navigation Bar > "Create (+)" > "Mixture" > "Medium Recipe"


2. Add composition of Medium Recipe by selecting the ingredients and their concentration values and units. 
    ```{tip}
    If your medium is composed of a mixture of pre-prepared solutions, create Medium Recipe entities for those solutions beforehand. This way you have detailed recipes for the intermediate solutions, and you can use them as ingredients for your media in Benchling as you do in the laboratory. 
    ```
3. Write recipe instructions.
4. Fill out relevant schema fields, of add your own in Custom Fields.
5. Add an alias (e.g., an ID for your media library).
6. Register!

### 2. Create a Medium Recipe from another Medium Recipe

````{raw} html
<iframe 
    width="560" height="315" src="https://www.youtube.com/embed/0xyTsDe8OKk?si=IblJFMTi19mk73Ao" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>
````

*Steps:*
1. Create a Medium Recipe entity, **link parent Medium Recipe in 'Derived from' field**, assign name and folder.

        Benchling Navigation Bar > "Create (+)" > "Mixture" > "Medium Recipe"


    ```{note}
    Alternative: Navigate to *MEDIUM RECIPE* tab from pre-existing Medium Recipe and create a Medium Recipe entity. New Medium Recipe will automatically be 'Derived from' parent Medium Recipe.
    ```

2. Modify the composition of the new Medium Recipe: add/remove ingredients, or change concentrations.  
3. Write recipe instructions.
4. Fill out relevant schema fields, of add your own in Custom Fields.
5. Add an alias (e.g., an ID for your media library).
6. Register!

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

 If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).
