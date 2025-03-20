# Electronic Lab Notebook (ELN)

 🎯 Learning goals
- Tools and functionalities inside an entry
- Templates and subtemplates
- Tips to structure/organize your ELN

## Introduction

Documenting experiments is an indispensable part of scientific research.

Much like the traditional paper notebook, you can open a blank entry of the electronic lab notebook (ELN) and start writing your experimental notes. However, the ELN is built to facilitate and elevate note taking, as it offers:

- Tools for structuring your notes
- Ability to connect notes to data in the LIMS, or to add external links
- Ability to create entries from templates
- History and version control
- Searchable notes

In this guide you will learn how to make the most out of the ELN capabilities to make experiment documentation easier and more powerful.

## Functionalities inside an ELN entry

Entries provide multiple formatting options and acessory functionalities that facilitate writing clear and well-structured experimental notes. Bellow you can learn about these functionalities in more detail, and you can try them out yourself with [this entry template].

```{figure} ../_static/images/eln-guide-5.png
:alt:
:width: 90%
:align: center
```

````{dropdown} Format text & Create lists

Similarly to other word processors, in the Benchling ELN you can: toggle headers, format text style and change text or highlight color. You can also create three types of lists: bulleted, numbered or with toggable checkboxes.

```{figure} ../_static/images/eln-guide-14.png
:alt:
:width: 90%
:align: center
```
````
````{dropdown} Section notes by calendar day
Supposedly there are "Sections" but I do not have that option.
Add a calendar day for your entry: adding new days causes the entry to span multiple days in your personal calendar

````

````{dropdown} Insert tables and perform calculations

Tables in the ELN allow you to perform calculations and format table similarly to other spreadsheet applications. Particularly, these tables support:
- Writing your **formulas** using '=' to begin, and anchoring cells in a formula with '$'.
- Using predefined **functions** (SUM, AVERAGE, MIN, MAX, COUNT, etc.).
- Converting to **scientific notation** and setting **decimal precision**.
- Dragging cell to **auto-fill numerical series**.
- Merging cells, and deleting/inserting rows or columns.
- Formatting cell and text colours.
```{figure} ../_static/images/eln-guide-12.png
:alt:
:width: 60%
:align: center
```
For more information, check out [Benchling guide Use tables in Notebook entries](https://help.benchling.com/hc/en-us/articles/9684274339597-Use-tables-in-Notebook-entries).

````

````{dropdown} Link within Benchling or to external URLs

**You can create internal links to Benchling entities, entries or users:** By typing "@", a prompt allows you to search and select the object within Benchling that you want to link, and you can do so within your text or tables. 
With internal links you can connect the entities in an experiment (strains, plasmids, primers, etc.) and the documentation of that experiment, enabling a more precise and systematical report. The relationships established between items across your project is shown in their Metadata section under "Relevant Items".

**You can also link to external URLs:** Integrate links to external URLs in the text of the ELN entry.

```{figure} ../_static/images/eln-guide-9.png
:alt:
:width: 90%
:align: center
```
````

````{dropdown} Attach external files and images

You can upload files up to 2GB directly into an entry. This is easily accomplished by either **drag-and-drop** or **copy-paste** of a file, or by clicking **Insert > Attachment > select file**. If larger files are needed, store them externally and link the file.

```{figure} ../_static/images/eln-guide-15.png
:alt:
:width: 70%
:align: center
```

Images are displayed directly in the entry, while attachements such as Word, Excel, Powerpoint, PDF and text files can be viewed in a tab that opens within the entry upon clicking on the file.

```{figure} ../_static/images/eln-guide-10.png
:alt:
:width: 70%
:align: center
```
````

````{dropdown} Annotate images

Benchling now allows you to annotate images within entries. When you click "Annotate image" you are given the option of adding **text**, **arrows** or **circles**, then dragging, re-sizing and coloring these elements.

```{figure} ../_static/images/eln-guide-11.png
:alt:
:width: 60%
:align: center
```
````



````{dropdown} Use structured tables

You can create your Benchling entities and inventory items directly in your ELN using structured tables. The available types of structured tables are the following:

- **Registration table**: create and register entities.
- **Inventory table**: move entities in boxes or plates.
- **Box Creation table**: create boxes.
- **Plate Creation table**: create plates.
- **Lookup table**: look up values from registry entities and inventory items.
- **Result table**: register results linked to entities.
- **Mixture prep table**: create Medium Batches from your Medium Recipes.

To insert a Structured table in your Notebook Entry, click on **"Insert"**, and select the table of interest:
```{figure} ../_static/images/eln-guide-16.png
:alt:
:width: 60%
:align: center
```

→ Learn how to:
- [Use structured tables to register Strains](strain_registration.md)
- [Use Mixture prep tables to create Medium Batches](media.md)

````

````{dropdown} Table of contents
Benchling automatically generates a dynamic table of contents to help you navigate the elements in your ELN, which is particularly useful for lengthy and complex notes. The order in which the table of contents is organized is: section, headers, tables and attachements.

```{figure} ../_static/images/eln-guide-17.png
:alt:
:width: 90%
:align: center
```
````

````{dropdown} History and version control 

Benchling automatically saves changes in your ELN. You can review the version history of your entry and if needed you can:
- **Restore the entry to a previous version** - e.g. because you accidentally deleted/added unwanted content.
- **Clone a version of the entry to a new entry** - e.g. because you want to try and compare different methodologies during part of an experiment.

```{figure} ../_static/images/eln-guide-18.png
:alt:
:width: 90%
:align: center
```

````



## Templates and subtemplates

Write in an unstructured manner, or give a structure to your notes manually, **or use templates**

(agility, reproducibility)

"What are Notebook Templates & Collections?

Benchling's Notebook application streamlines the documentation of study observations and data, and ensures your scientists remain in compliance with established protocols. These benefits can be directly realized via the use of Notebook Templates and Collections, which standardizes the layout of entries for well-defined experimental workflows in your organization.

Notebook Templates are pre-formatted entries that aid in ensuring consistency, completeness, and compliance across an organization. There are created just like other entries, and provide benefits including:

    Ensuring necessary data for a study are captured with Structured Tables
    Providing review criteria to ensure completeness before entry approval
    Categorizing entries and attaching metadata with Entry Schemas

Notebook Collections are folders that house a group of Notebook Templates, and can be managed by your team's designated admins or leads."

## Tips

Use `/` shortcut to insert elements to entry.