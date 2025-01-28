# Create a plate map

Benchling plate mapping is a useful tool for planning, visualising and registering your plate experiments:

- You can add multiple layers of annotations and values to create a digital record of your plate experiment.

- You can insert the resulting map in your ELN and navigate through the different variables in the wells.

- You can access or search the plate data stored the inventory.

```{figure} ../_static/images/plate-map-1.png
:alt: Demonstrates layers of annotation that plate maps can have
:width: 80%
:align: center

*Example of layers of annotations in a plate map*
```

## Pre-requesites

Before creating the Plate Map, make sure the contents you want to fill the plate with are [registered](https://biosustain.github.io/benchling-resources/guides/use_registry.html) and containable (see note for list of containable entities). You can also add those entities to a worklist to facilitate filling up the plate in bulk. 

````{dropdown} List of Containable Entities

List of Benchling entities that are containable - i.e., can be added into containers (Bottle, Cryovial, Well, etc.):

- Analytical Submission Sample 
- Cell Line Batch 
- Cell Line Design 
- Commercial Material 
- Confidential Compound  
- Confidential Compound Batch 
- DNA Fragment Batch 
- Strain Batch 
- Plasmid Batch 
- Fermentation Culture 
- Generic Sample / Cell Pellet 
- gDNA  
- Media Samples 
- Medium Prep 
- Microbiome Diluted Sample 
- Microbiome Diluted Sample in Media 
- Microbiome Sample 
- Nanopore Sequencing Submission Sample 
- Primary Cell Batch 
- Primer 
- Primer Pair Mix 
- Protein Batch 
- Protein Sample 
- Proteomics Submission Sample 
- Stem Cell Batch 
- Timepoint Sample 
````

## Steps to create a plate map

To create a plate map, you can either insert it into a notebook entry (*Insert > Plate Map*) or create a plate in the Inventory (*Create > Plate*). This opens an interface where you can carry out the plate mapping in three major steps:

### 1. Select the fixed plate
Choose between 6-well, 12-well, 24-well, 48-well, 96-well, or 384-well plates. Designate a location in the inventory, or fill other fields for that plate schema.

### 2. Annotate the wells in the plate
Select multiple wells at once by dragging the cursor or by using the *shift* key, or fill wells individually.
- **Add the well contents** from the registry or from your worklist.
- **Assign roles to the wells**: samples, controls, blanks or standards.
- **Add additional labels with the Well schema fields**: Treatment and Dilution Factor.

### 3. Specify the concentrations and volumes of your contents
Indicate the values for the contents filling up the plate in your experiment: total well volume, stock concentration, transfer volume and well concentration.


**Follow along this video demonstration of creating a plate map in a notebook entry.**

````{raw} html
<div style="text-align: center;">
<iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/p_TlsnvtSxE?si=7GoysTqS336TJgnx"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>
</div>
````
