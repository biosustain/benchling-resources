# Start here!

This guide will introduce you to the **main features and concepts of Benchling**, helping you navigate the platform and manage your research data effectively.

## Navigate Benchling

Benchling’s interface includes a main <mark style="background-color: #C5DBEC;">Navigation Bar</mark> on the left-hand side of the screen. To identify an icon, hover over it to reveal its **label**, and click to view its contents.

```{figure} ../_static/images/hover-on-navigation-bar.png
:alt: The navigation bar
:width: 60%
:align: center

*The navigation bar*
```

## Register your data

When working on a project, you will often create various *entities*, such as primers, strains, and plasmids. Your entities might or might not be *registered*. 

When an entity is registered, it enters the <mark style="background-color: #C5DBEC;">Benchling Registry</mark>.

```{figure} ../_static/images/register-plasmid.png
:alt: Registering my plasmid
:width: 80%
:align: center

*Registering my plasmid*
```

````{dropdown} The Registry

**Registering** your entities ensures they are easily searchable and accessible across the organization, while also standardizing metadata capture.

When you register an entity (for example, a strain), you unlock additional features:
- tracking the entity location by using the **Inventory** feature
- establishing links between the entity and other registered entities (e.g., its parent strain)
- recording results related to the entity

```{figure} ../_static/images/data-storage.png
:alt: Diagram showing the meaning and relationship between Registry, Inventory and Results
:width: 80%
:align: center

*The Registry, Inventory and Results*
```

**Important things to consider**

→ *You can register many kinds of entities*

The Registry goes beyond biological samples. It can also be used for things like media, commercial materials and submissions for analytics. 

→ *Registering lets you keep track of entities*

By using the Registry, you can keep track of links between entities, for example, if you have a parent strain and the plasmid it was transformed with to get a new strain, you could link all three entities. 

You can also monitor the storage of samples. For storage, you can create batches, which represent physical instances of an entity. Batches let you know when something was stored and by whom.

```{figure} ../_static/images/transformation-storage.png
:alt: Diagram showing the meaning and relationship between Registry, Inventory and Results
:width: 80%
:align: center

*Relations between entities*
```

→ *Some entities require pre-registering other entities*

For example, if you desire to link a plasmid when registering a new strain, the plasmid must be registered beforehand. 

````

## Track your samples' location

You can track the location of your entities in Benchling (for example, by specifying in which **box** and **freezer** a sample is stored) using the <mark style="background-color: #C5DBEC;">Benchling Inventory</mark> feature.

````{dropdown} The Inventory

The **Inventory** is a virtual representation of the storage system of the labs at DTU Biosustain. It allows user to track the physical location of registered entities. 

Using the Inventory requires a few essential steps. First, you must create a box or a plate in the location (room, freezer) you want your samples to be. This can be done from the Inventory menu or from an ELN. Afterwards, you need to store your registered entity in a container, such as a tube or a vial. Alternatively, if you want to store a sample in a plate, only the plate needs to exist beforehand.

```{note}
Entities such as **strains** or **plasmids** require **Entity Batches** to be created before storage. This makes it possible to know when a particular physical instance of the entity was stored.
```

A general overview of the information related to the inventory is shown in the figure below.

```{figure} ../_static/images/storage-inventory.png
:alt: Diagram showing the meaning and relationship between Registry, Inventory and Results
:width: 80%
:align: center

*Inventory overview*
```
````
```{figure} ../_static/images/a-box.png
:alt: Image of a box in Benchling
:width: 80%
:align: center

*Example of a 9x9 Box in Benchling*
```

## Use structured tables

You can create your **Benchling entities** (like strains and cultures) and **inventory items** (like boxes and plates) directly in your Electronic Notebook using <mark style="background-color: #C5DBEC;">Structured tables</mark>. 

````{dropdown} Types of structured tables

Here are the available types of structured tables that you can add to your Electronic Notebook:

- *Registration* table (to create and register entities)
- *Inventory* table (to move entities in boxes or plates)
- *Box Creation* table (to create boxes)
- *Plate Creation* table (to create plates)
- *Lookup* table (to look up values from entities and inventory items)
- *Result* table (to register results linked to entities)

```{note}
Registration tables enable you to create multiple entities at the same time. The generated entities will be **automatically added to the Registry**, without the need to manually register them.
```
````
→ Check out [this guide](strain_registration.md) to learn how to use Structured tables to register and store Strains. 

To insert a Structured table in your Notebook Entry, click on **"Insert"**, and select the table of interest:

```{figure} ../_static/images/insert-button.png
:alt: Image showing how to insert a table in the ELN
:width: 80%
:align: center


```

## Track your results 

You can track your experimental results either in an open, unstructured text format in the Electronic Notebook or in a structured format using Structured tables.

````{dropdown} Results

Structured results can be recorded in Benchling using **Result tables**. Result tables, similarly to Registration tables (used to create and register entities to which the results are linked to) are created and used within the Electronic Notebook. 

**Results** are linked to entities in the following way:

```{figure} ../_static/images/results-example.png
:alt: Diagram showing the meaning and relationship between Registry, Inventory and Results
:width: 80%
:align: center

*Figure adapted from Benchling*: [Results Best Practices](https://help.benchling.com/hc/en-us/articles/15656552131085-Results-Best-Practices)
```
````

## Categorize your data

<mark style="background-color: #C5DBEC;">Benchling Schemas</mark> are the structural foundation for how data is collected and categorized in Benchling, and ensure a center-wide, uniform approach to data collection. 

````{dropdown} **Benchling Schemas**

In Benchling, **schemas** play a central role in how information is structured, standardized, and interconnected. They act as **templates** that define the organization of biological, chemical, and material data.

While *entities* represent the individual components of your research (such as DNA sequences, strains, or reagents), *schemas* determine how those entities are structured and managed. They specify the required fields, optional properties, and relationships between entities, serving as the foundation for capturing and organizing information effectively.  
````

## Search data in Benchling

You can search across the data that you have access to using the <mark style="background-color: #C5DBEC;">Search functionality</mark>. 
This search bar enables you to type keywords or exact names to find what you are looking for. To make your search easier, you can filter by data type, author and many other parameters. 
You can also limit your search by selecting a single project of interest. 

```{figure} ../_static/images/search-bar.png
:alt: Search functionality
:width: 80%
:align: center

Use filters to make your search more accurate (e.g., filter by "Strain") 
```


