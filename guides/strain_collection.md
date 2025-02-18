# Register a strain collection in Benchling

🎯 This guide will show you how to **upload an entire strain collection** from a spreadsheet to Benchling following a **Notebook template**.

```{dropdown} You may want to do this if...
* You have an externally stored collection (for example, in a spreadsheet) and you’re interested in sharing with others through Benchling

* You want to be able to link strains in your Notebook entries (also referred as "tagging" in Benchling, e.g., *@MyStrain*)

* You want to keep track of the links between parental and child strains, therefore create a lineage of your strains

* You’d like to keep a record of where all your strains are stored and when they are used

* You’d like to upload strain-related metadata to Benchling at the end of a project or before leaving Biosustain, to make sure that data is not lost over time

* You’d like to promote FAIR data! 😄
```

⚠️ If you need to register only a few strains, and not an entire strain collection, you might find it easier to follow this [guide](strain_registration.md) instead.

## Before starting

The only prerequisite to the following steps is to **have a spreadsheet** with metadata related to your strains.

## Template overview and guide

1. **Create a Notebook entry based on the template.**
    
    You will need the Registration of Strain Collection template, which you can find under the LIMS Support folder, as seen in the picture below.

    ```{figure} ../_static/images/straincol-template.png
    :width: 90%
    :align: center

    ```

    The template should look like this:
    
    ```{figure} ../_static/images/template-overview.png
    :width: 90%
    :align: center

    ```

2. **Watch the video to understand how to use the template.**
    ````{raw} html
    <div style="text-align: center;">
    <iframe 
        width="600" 
        height="350" 
        src="https://www.youtube.com/embed/dTW0_-R111Q?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
    </iframe>
    </div>
    ````

## Troubleshooting


```{dropdown} If you run into any issues while registering your collection, read through this list and see if you can find a solution. 

* **General tip:** Refresh the Benchling tab you are working on. This can help when entity links are not being detected properly.

* *"I submitted a registration table and realized the entities were saved to an unwanted place."* 

    * By default, the entities will be saved to the folder where the template ELN is located. This can be changed in the **Registration table settings**.

    * These settings can only be modified **before submitting entities**. If you made a mistake, you will have to move them manually to the desired location; and create a **new table** for future entities of the same schema that you’d like to register.

* *"While setting up a registration table, I deleted a column that is important for me. How do I bring it back?"*

    * This can be done easily by following these steps:

        * *Right click > Insert column left/right > Select the column you’d like to bring back*

* *"I can’t find a field that matches my spreadsheet on the registration table."*

    * First option: look for a field that could allow for the type of data you want to store and add a note on your ELN regarding this. 

    * Second option: Add a custom field/column

        * This only supports the following data types: text, integer, decimal, boolean, date, and datetime.

    * Third option: Reach out to us to potentially add a new field to the schema. This may or may not be possible.

* *"I registered some plasmids that are not in Benchling, and now I’d like to upload the sequences to the corresponding entities. How can I do this?"*

    * You can update your registered plasmid entities with the **“Reimport DNA sequences in bulk”** option. 
    
    ````{figure} ../_static/images/reimport-DNA.png
    :width: 80%
    :align: center

    ````

    * You only need to upload a file with the same filename as the entity name, and the entity will be updated accordingly, keeping the fields that had already been filled.
```

If you have any other problem, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk)!

## Additional resources


```{dropdown} Links that could be helpful
* Once your collection is uploaded to Benchling, you can use lookup tables to easily find specific information related to your strains in your experiment ELNs. 

    * [Lookup Columns and Tables – Benchling](https://help.benchling.com/hc/en-us/articles/9684194769421-Lookup-Columns-and-Tables)


* If you’d like to know more about the inventory system in Benchling and how you can use it to track your strains, you can check out the Benchling guides.

    * [What is the Inventory? – Benchling](https://help.benchling.com/hc/en-us/articles/9684234442509-What-is-the-Inventory)

    * [Using your inventory – Benchling](https://help.benchling.com/hc/en-us/articles/9684234442509-What-is-the-Inventory)
```