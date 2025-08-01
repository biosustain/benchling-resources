# Understand the Registry

🎯 This guide will help you understand how to use the Benchling Registry according to your needs. 

## Why use the Registry?

Using the Registry might seem like a daunting task, but it is quite flexible, and **it comes with many benefits**, including:
- the **ability to assign distinct data types** to samples, containers, and results, ensuring that data is easy to find and interpret
- the possibility of **standardizing metadata fields** across the organization, so data types like plasmids or strains have consistent and uniform metadata.

**Registering your experimental data in the Benchling Registry** is a big step towards its standardization and its long-term **findability** (by you and other colleagues).

You might have already recorded your experimental data in your Electronic Notebook, in sequence files (for example, in the case of plasmids) and/or in spreadsheets. All of these can be standardized and added to the Registry.

```{figure} ../_static/images/registry-sources.png
:width: 50%
:align: center

*Sources of information for the Registry*
```

## Choose a registration method

The choice of registration method depends on your particular needs. 

Generally, it is recommended to use **registration tables**, which can be added to an ELN, because they are a convenient way to visualize and keep track of all registered entities and related metadata. 

Nevertheless, if you’d like to explore different options, you can refer to the flowchart below to get some guidance on the **recommended methods** for different scenarios. 

```{figure} ../_static/images/registry-options.png
:width: 90%
:align: center

```

```{caution}
It is important to note that entities **registered** outside of registration tables **cannot be updated via registration tables**. For updating of these entities, it is necessary to go to their metadata tab individually, or to use [bulk actions in the registry](https://help.benchling.com/hc/en-us/articles/9684264620941-Export-Registry-data-in-bulk) to modify larger amounts of registered entities.  
```

## A reminder: Set the schema!

Setting the **schema** of an entity is a **crucial** step which is **always** required for registration. If you create new entities in Benchling, such as DNA sequences, plasmids or primers, **remember to set their schema**! This can save you a lot of time later. 

## How to register…

### a. From your ELN (with registration tables)

```{Note}
If you’d like to familiarize yourself with a comprehensive start-to-finish example of registration and storage from an ELN, you can check out the article on [Strain Registration](https://biosustain.github.io/benchling-resources/guides/strain_registration.html).  
```
The easiest and most traceable way of registering is from your own Notebook. You can create an ELN meant for all your registrations, or register entities by experiment or day. 

1. **Insert a registration table**

    *Your ELN > Insert > Registration table*

    You may choose to create new entities or register existing ones.

```{Note}
To register an existing entity, its **schema** must be set correctly (eg. plasmid, DNA fragment, primer, etc.) You can do this from your entity file: *Metadata > Schema*
```
Registration tables are created by schema. If you’d like to register entities with different schemas, you will need multiple tables.

```{figure} ../_static/images/select-schema-registrationtable.png
:width: 80%
:align: center

```
2. **Fill in the fields that are relevant for your workflow**

    Some fields are mandatory, and many are optional. It’s recommended to fill in as much information as possible, so other users can know what the purpose of a given entity is.

3. **Check for validation errors and submit**
    You will be able to submit your entities to the registry once all required fields are full.

```{figure} ../_static/images/reg-table.png
:width: 80%
:align: center

```
If there are any oversights, Benchling will indicate that there is a value error:
    
```{figure} ../_static/images/value-error.png
:width: 50%
:align: center

```

```{caution}
Value errors may occur *after* registration if an entity that is referenced in one of the fields is archived.
```

### b. Directly from an entity

This option is mostly useful when working with only a few entities. For example, if you are designing a single plasmid, you might want to fill the relevant schema fields to avoid missing or forgetting about important information. 

1. Click on the entity’s Metadata tab
2. Set the schema (if not done previously)
3. Fill in the schema fields
4. Register the entity

````{raw} html
<div style="text-align: center;">
<iframe 
    width="700" 
    height="320" 
    src="https://www.youtube.com/embed/ubmvfK-iqEs?si=2cv50WMQRTln9Onl?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
</iframe>
</div>
````

### c. From your project folder

This option is similar to b), in the sense that it reduces the amount of clicks needed to register several pre-existing entities. 

1. Open the expanded project view
2. Select the entities you want to register 
3. Click the registration button

````{raw} html
<div style="text-align: center;">
<iframe 
    width="700" 
    height="320" 
    src="https://www.youtube.com/embed/YLivrYSQVBg?si=RUzvdjpYNPpVtoP4?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
</iframe>
</div>
````

### d. From the Registry menu

If you have a spreadsheet containing metadata for unregistered entities, you can upload the information directly from the registry menu. This feature allows you to create and register these entities in one seamless step.

This approach is especially useful when managing large datasets, as it allows for bulk actions on registered entities. so you can quickly register new entities or update pre-existing ones with ease. All you need is a properly formatted spreadsheet that aligns with your schema fields, ensuring that your data integrates smoothly into the system.

```{Note}
Make sure your spreadsheet's columns match the schema fields, although additional fields can be omitted when uploading. This step ensures that your data is mapped correctly during the upload process.
```

````{raw} html
<div style="text-align: center;">
<iframe 
    width="700" 
    height="320" 
    src="https://www.youtube.com/embed/bvRfALTDH_I?si=mJD0LWR1uXEIMVcQ?rel=0&modestbranding=1&autoplay=0&showinfo=0" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
</iframe>
</div>
````

## Recommendations

- Create a structured ELN where you can keep track of your registrations.

    - This could be done for each big project or experiment. This way, you will be able to see all the entities you have generated and registered in a single place. Additionally, this can facilitate the storage process. 

    - You can register from a table multiple times, without duplicating registries – only the changes and additions are uploaded.

If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).