# Benchling essentials


🎯 This guide will introduce you to the **core concepts of Benchling** that will support your data registration efforts and, generally, ease potential struggles in using the platform.

For a **more extensive introduction** to Benchling and its **Molecular Biology Tools** functionalities (including **construct design, construct assembly, sequence alignment**, **CRISPR tool**), check-out these [training materials](/training_materials/basics.md)!

## Navigate Benchling

Benchling’s interface includes a main <mark style="background-color: #C5DBEC;">Navigation Bar</mark> on the left-hand side of the screen. To identify an icon, hover over it to reveal its **label**, and click to view its contents.

```{figure} ../_static/images/hover-on-navigation-bar.png
:alt: The navigation bar
:width: 60%
:align: center

*The navigation bar*
```

## Use the Notebook

Benchling includes an <mark style="background-color: #C5DBEC;">Electronic Notebook functionality</mark> that enables you to take experimental notes, create SOPs and share them with your team.

To start taking notes on your experiment, you need to create a **Notebook entry** (this is the way Benchling calls a "page" of the Electronic Notebook). Instead of creating an empty Entry every time you start a new experiment, we suggests you to create **Notebook template/s** that can be reused for all your experiments, saving you time and facilitating **structure** similarity across entries.

```{figure} ../_static/images/eln.png
:alt: Example of a Notebook entry
:width: 80%
:align: center

*Example of a Notebook entry*
```

<br/>

````{dropdown} More on Notebook templates

In order to avoid having to start from a blank page every time you create a Notebook entry, we suggest you to create one or more Notebook **templates** (or a **Notebook sub-templates**) that you can reuse.

Benchling has dedicated **guides** on templates and sub-templates, check them out here:

→ [Create a new template](https://help.benchling.com/hc/en-us/articles/9684282597645-Creating-entry-templates-and-template-collections)


→ [Create a new sub-template](https://help.benchling.com/hc/en-us/articles/13937915100301-Reusing-content-with-sub-templates)

````



## Register your data

When working on a project, you will often create various *entities*, such as primers, strains, and plasmids. Your entities might or might not be *registered*. 

When an entity is registered, it enters the <mark style="background-color: #C5DBEC;">Benchling Registry</mark>.

```{figure} ../_static/images/register-plasmid.png
:alt: Registering my plasmid
:width: 80%
:align: center

*Register a plasmid*
```

<br/>

````{dropdown} More on the Registry

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

```{figure} ../_static/images/a-box.png
:alt: Image of a box in Benchling
:width: 60%
:align: center

*Example of a 9x9 Box in Benchling*
```

<br/>

````{dropdown} More on the Inventory

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

## Use structured tables

You can create your **Benchling entities** (like strains and cultures) and **inventory items** (like boxes and plates) directly in your Electronic Notebook using <mark style="background-color: #C5DBEC;">Structured tables</mark>. 

To insert a Structured table in your Notebook Entry, click on **"Insert"**, and select the table of interest:

```{figure} ../_static/images/insert-button.png
:alt: Image showing how to insert a table in the ELN
:width: 80%
:align: center

*Insert a Structured table*
```

<br/>

````{dropdown} More on Structured tables

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
→ Learn how to [use structured tables to register Strains](strain_registration.md)

````



## Track your results 

You can track your experimental results either in an open, unstructured text format in the Electronic Notebook or in a structured format using <mark style="background-color: #C5DBEC;">Result tables</mark> (one of the different types of Structured tables).

```{figure} ../_static/images/result-table.png
:alt: Image showing how a result table looks like in the Notebook
:width: 100%
:align: center

*Example of a Result table in the Notebook*
```

<br/>

````{dropdown} More on Result tables

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

```{figure} ../_static/images/schemas.png
:alt: Image showing the meaning of schemas
:width: 80%
:align: center

*Example of sample schemas for sequences*

```

<br/>

````{dropdown} **More on Benchling schemas**

In Benchling, **schemas** play a central role in how information is structured, standardized, and interconnected. They act as **templates** that define the organization of biological, chemical, and material data.

While *entities* represent the individual components of your research (such as DNA sequences, strains, or reagents), *schemas* determine how those entities are structured and managed. They specify the required fields, optional properties, and relationships between entities, serving as the foundation for capturing and organizing information effectively.  

````

## Search data in Benchling

You can search across the data that you have access to using the <mark style="background-color: #C5DBEC;">Search functionality</mark>. 
This search bar enables you to type keywords or exact names to find what you are looking for. To make your search easier, you can filter by data type, author and many other parameters. 
You can also limit your search by selecting a single project of interest. 

```{figure} ../_static/images/search-bar.png
:alt: Search functionality
:width: 70%
:align: center

*Use filters to make your search more accurate (e.g., filter by "Strain")* 
```


## Browse the terminology

If you are unsure about the meaning of a term in Benchling, here you can find a <mark style="background-color: #C5DBEC;">complete list of Benchling terms</mark> and the correspondent description. If you have questions on any of the terms, please [contact us](../contact.md).

````{dropdown} Benchling terms list

| Term | Description |
| ---- | ----------- |
| Entity | Structured data object. There are default Benchling entities (e.g. DNA Sequence, Amino Acid Sequence, Oligo) and Custom Entities. Entities can be created and stored within Projects, formally registered in the Registry or assigned Inventory locations. |
| Entry | Notebook page for research documentation. Can contain text, tables, images and links to Benchling entities. |
| Schema | Defined data structure of Entities, Entries, Workflows, Requests or Automation runs. A schema comprises a set of fields that captures relevant properties of an object, including tracking its relationships with other objects within Benchling. |
| Project | Folder for storing and organizing materials created in the development of a research project: ELN entries, biological entities, protocols. Permissions can be managed to facilitate collaboration. |
| Registry | Database with the biological materials used/created in research projects at DTU Biosustain, where metadata is searchable and standardized. When an entity is registered, it is formalized within the system through the assignment of an unique ID and the storage of its metadata in structured manner (i.e., within a schema). |
| Inventory | Represents the physical storage system of samples and reagents at DTU Biosustain, and is used to manage and track these items at the center: their location, container, quantity, usage history. |
| Worklist | List of samples facilitating transfer of entities between applications and performing actions in bulk. |
| Sequence | (entity type) DNA, RNA, Amino Acid or Oligo sequence which can be processed with Benchling’s molecular biology design and analysis tools. There are currently 9 sequence entity schemas. |
| Custom Entity | (entity type) Entity created using a “custom schema” developed at Biosustain based on researchers needs and most used sample types. There are currently 49 custom entity schemas. |
| Mixture | (entity type) Solution comprised of multiple ingredients where the exact quantities of each ingredient are tracked. There are currently two mixture entity schemas: Medium with recipe and Medium prep.  |
| Container | Represents physical containers such as tubes or wells that hold biological samples or reagents, and tracks concentration and volume of the contents. |
| Box | Structured inventory type that is assigned a location, representing boxes stored at the center. Technically functions as a grid of containers of fixed dimension (i.e., with a max number of containers it can hold).  |
| Plate | Structured inventory type that is assigned a location, representing plates stored at the center. Technically functions as a grid of well containers, and can be “matrix” or “fixed” depending on whether well containers can or cannot be moved within the plate, respectively. |
| Template | Predefined entry structure used to facilitate writing specific and recurrent types of entries. Templates can be created by Benchling admin or users themselves.  |
| Subtemplate | Entry section with predefined structure that is inserted into entries. Subtemplates can be created by Benchling admin or users themselves. |
| Protocol | Structured document used to detail experimental procedures. Can be linked to notebook entries. |
| Dropdown | Data type consisting of a predefined list of values, useful for standardizing metadata options.  |
| Workflow | New workflow management system that enhances collaboration by linking together sample processing steps in a single workflow. Each step (also called “workflow task”) can be executed by different researchers. |
| Workflow Task | Single processing job within a workflow. Each task has standard operational properties and custom fields that represent the parameters required to do the job. |
| Legacy Workflow | Legacy workflow management system that connected different notebook templates to facilitate high-throughput sample tracking. Substituted by Workflow module. |
| Legacy Request | Legacy request system that enabled submission of standardized requests to colleagues (e.g., a lab purchasing order or a sample analysis). Substituted by the Workflow module. |
| Automation Run | Action performed through a lab instrument, or by a user in the Notebook. This action can, for example, automatize the transformation of a spreadsheet to facilitate data ingestion and extraction to/from lab robots or other instruments. |
| Benchling Connect | System that enables Benchling to link to instruments in the lab and ingest/export data from them. |
| Results | Tables that capture experimental results in a standardized manner through custom schemas created by Benchling admin, and that can link those results to samples in the registry. |
| App Canvas | Blocks programmed to provide specific features through an interactive interface inserted in notebook entries. These can be particularly useful for interacting with external systems - e.g., allow user to import data on a chemical from PubChem in their notebook. |
| Benchling App | External application integrated into Benchling’s platform.  |
````

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).