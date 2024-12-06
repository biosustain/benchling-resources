# Overview

````{dropdown} **Data collection and storage in Benchling**

**The Registry**

When working on a project, you will often create various entities, such as primers, strains, and plasmids. **Registering** these entities ensures they are easily searchable and accessible across the organization, while also standardizing metadata capture. 

This registration process is crucial for utilizing the **Inventory** feature, which helps track entities and their usage over time. Additionally, registering enables you to establish relationships between entities and link them to **Results** tables for comprehensive data analysis. 

Knowing how to use the Registry will allow you to unlock the full capabilities of Benchling!

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

**The Inventory**

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

**Results**

**Results** tables can be created in ELNs. They allow you to capture and map specific results back to samples in the Registry. 

An example of how **Results** can be used in Benchling is shown in the figure below:

```{figure} ../_static/images/results-example.png
:alt: Diagram showing the meaning and relationship between Registry, Inventory and Results
:width: 80%
:align: center

*Figure adapted from Benchling*: [Results Best Practices](https://help.benchling.com/hc/en-us/articles/15656552131085-Results-Best-Practices)
```

````

````{dropdown} **Entities and schemas in Benchling**

In Benchling, **entities** and **schemas** are the backbone of how information is structured, stored, and interconnected. They provide a standardized way to represent biological, chemical, and material components, enabling seamless workflows and robust data tracking. Together, entities and schemas ensure that data remains organized, traceable, and easily accessible throughout your research processes.

**Entities**

Entities are the individual building blocks of the Benchling platform, representing key elements of your research, such as DNA sequences, strains, samples, or reagents. They hold information about physical or conceptual items in the lab, often enriched with metadata like descriptions, annotations, and relationships to other entities. 

**Schemas**

Schemas define the structure of entities in Benchling, acting as templates that standardize how information is captured and stored. They determine the required fields, optional properties, and relationships for a given type of entity. 

````