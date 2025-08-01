# Manage your Benchling Project

🎯 This guide will show you how to manage Benchling Projects to keep research data **structured** and **accessible**. It will aslo outline good practices to improve **reusability** of your data after your stay at DTU Biosustian. 

## What are Projects in Benchling?
**Project folders** (referred to as *Projects* in this guide) are key elements of data management in Benchling that **provide a structure** to the data registered in Benchling.

Each Project has its own **Permission** settings that allow the Project Admin to define who will be able to access the data inside the Project (the Project **Collaborators**). It is possible to grant access to:
- a single user (e.g., a colleague) 
- an entire team (e.g., your research group)

Go to the section *"Add and remove Collaborators"* to learn how manage the Project permissions.

It is possible to further organize the data within the Project by creating **Subfolders**.
In these folders you can store:
- notebook entries
- protocols
- entities (e.g., plasmids, oligos, and DNA sequences)

```{figure} ../_static/images/projects1-project-structure.png
:width: 60%
:align: center
*Example of the structure of a **Project folder***

```

````{admonition} ℹ️​ Need a Training space?
:class: my-custom-admonition
If you want to try out some of Benchling's functionalities, you can use the [Biosustain Training](https://biosustain.benchling.com/biosustain/f_/xmPebKow-biosustain-training/?filter=section%3Aall%3Bfolder%3Alib_xmPebKow%3Btypes%3AIS_ONE_OF%3Afolder%2Centry%2Cprocess%2Cprotocol%2Cbulk_assembly%2Cbasic_folder_item%2Cprotein%2Cmixture%2Csequence%2Crna_sequence%2Coligo%2Crna_oligo%2Canalysis%2Cdataset%3BarchivePurposes%3AIS_ONE_OF%3ANOT_ARCHIVED%3BisAssociatedWithUnsubmittedRequestV2Submission%3AIS_FALSE%3BProcessesIsSystemDataFilter%3AIS_FALSE&offset=0&limit=50&sorts=starred%3A0%3Bname%3A0&q=&v=2) project folder for this purpose. 
````

## Create a Project (or use an existing one)

All users can create Projects in Benchling, but new Projects should be created when truly **necessary**, for example when starting a new research project with a specific set of collaborators.

Each team might have a different preference on how they want to handle their Projects:

- Some teams create one Project **for each team member**
- Some teams create one Project **for each ongoing study**

### Recommendations 

#### ✅ Create one Project for each ongoing study, rather than for each team member.

Here are some of the **benefits**:

- The **entirety of the data related to that Project can be found in a single location**, avoiding redundancy and data scattering across personal folders.

- Easier **permissions management**
        
    🔐 All the **Collaborators can be added only once** (and easily updated), and they will always be able to find and access newly created data, avoiding unnecessary emails and access requests.
<br/><br/>

#### ✅ Whenever possible, add your (Benchling) Team as Collaborator to the Projects you create.

Here are some of the benefits:

- **Increased visibility** of your data and its findability

- Creation of a **centralized list** of your team's Projects, accessible by you and your PI at any time.

    📚 Access the **full list of your team's Projects** using one of the Menus shown below:

```{figure} ../_static/images/projects4-shared-projects-overview.png
:width: 100%
:align: center

*Different ways of having an overview of the Projects shared with your team*

```

````{dropdown} ℹ️​ Sharing samples with the Analytics team

When submitting samples for the Analytics team, it is necessary to grant them "Write" permission to your folder. Many users choose to create dedicated Projects for this. 

We recommend creating a **single, team-wide folder** to create samples for analysis. 

````

#### ✅ Manage team's protocols and other shared data by creating a Team-level Project.

In addition to having single Projects for each ongoing study, many teams have found it useful to have a **shared team Project folder** to ease the process of sharing protocols, team guidelines and other commonly shared information that is useful to the whole team.

This Project should have your (Benchling) Team in the list of Collaborators.

- All **new employees** added to the (Benchling) Team will **automatically gain access to all protocols** and relevant team-level information and data. 

```{figure} ../_static/images/projects5-team-project.png
:width: 80%
:align: center

*An example of a shared team Project folder*

```

## Add and remove Collaborators
Through the **Manage access** menu, you can define which users or teams can have access to your information, and what level of access each should have. 

```{figure} ../_static/images/projects2-manage-access.png
:width: 100%
:align: center
*View of the Manage Access menu*

```

````{dropdown}  Permission levels overview
The actions users with different levels of permissions can take are outlined below:
```{figure} ../_static/images/projects6-permissions.png
:width: 90%
:align: center

```
*Note: Users with append permission may be able to create blank entries, but they will then not be able to edit them. This permission may only be useful to append already completed documents and entities that do not require further editing by the user with this level of permission.*

````

`````{dropdown}  Granting access to a Team: Admins vs. Members

You can also specify separate levels of access for **members** and **admins** of a team. This may be useful if you would like to ensure a link between your Project and your team, but you can’t share the data with the entire team yet. 

To do this, locate the team you want to manage the permissions of in the **Manage access** menu of your Project, and follow these steps:

*More options button (…) > Add admin member access policy > Select level of access for users and admins*


```{figure} ../_static/images/projects3-admin-policy.png
:width: 80%
:align: center

*Setting an admin member access policy*

```
`````


## Identify your data requirements

Throughout your stay at Biosustain, it is good to keep in mind the **purpose** of the information you generate and store within Benchling, and how you (and others) will need it in the short, medium and long term. This information will determine how you register and structure your data in Benchling.

<div class="admonition my-custom-admonition">
  <p class="admonition-title">☑️ Checklist: </p>
  <p>Some questions to guide you through the process of <strong>managing your data</strong> (both within and outside of Benchling) are:</p>
  <ul style="margin-top: 0.4em; margin-bottom: 0.5em; padding-left: 2em; list-style-type: disc; font-size: 0.9em;">
    <li style="margin-bottom: 0.2em;">If external collaborators ask for some data after one year of running an experiment, can I find it easily?</li>
    <li style="margin-bottom: 0.2em;">Can my colleagues understand my experiments and find their results?</li>
    <li style="margin-bottom: 0.2em;">Is there an easy way to find items like strains or plasmids in the freezers?</li>
    <li style="margin-bottom: 0.2em;">Can I know if someone has a plasmid I need without asking everyone?</li>
    <li style="margin-bottom: 0.2em;">If I left right now, could people know where I left off and continue my work easily?</li>
  </ul>
</div>


## Additional tips for day-to-day usage

This section covers some suggestions for your day-to-day use of Projects in Benchling.

### Requests for access

You may receive emails requesting access to your Project folder. The format of these emails is the following:

        [User] has requested to be added to [Project folder], so that they can access [Entry or entity]. To grant access, add them as a collaborator on the project, add them to a team that already has access, or move the item to a project that they already have access to."

As the message states, if it is a user that should be on your (Benchling) Team, ask a Team admin to add them via the **Team** page. If that is not the case, you can grant them individual permission through the **Manage access** menu. 

### Browsing data

There are two main ways to browse through Benchling entries and entities:

- Within a Project, you can use the search bar to find contents, including items in subfolders. 

```{figure} ../_static/images/projects7-browse-projects.gif
:width: 80%
:align: center

```

- Through the Global Search, you can browse through all data types in Benchling across all the Projects you have access to. 

    * 🎯 Set the data type and add relevant filters first and then, if needed, filter by Project or Subfolder.

```{figure} ../_static/images/projects8-global-search.gif
:width: 80%
:align: center

```

- **Saved searches** can come in quite handy when you need to apply the same filters again and again. 

    ````{admonition} ℹ️​ TIP
    :class: my-custom-admonition
    After applying the needed filters, **save your Search and link it directly in your ELN entry** so you can find relevant entities without leaving your notebook. 
    ````

```{figure} ../_static/images/insert-saved-search.png
:width: 80%
:align: center
*Add a Saved Search as a link in your ELN entry*
```

### Use attachments to your advantage

You can attach files to your ELN, with a limit per attachment of 2 GB. While these files are not findable in Benchling through the global search, it may be useful to keep track of which files were generated in a given day.

````{admonition} ℹ️​ TIP
:class: my-custom-admonition
Use the *“Open preview”* button to view attachments directly in the ELN entry.
````

```{figure} ../_static/images/projects9-attachments.gif
:width: 80%
:align: center

```

### Maintain collections

While you may create and store plasmid, strain and primer collections externally (for example, in a spreadsheet shared through OneDrive), it is recommended to periodically update them to the Benchling Registry. 

You may find the following guides helpful for this purpose:

* [Understand the Registry — Benchling resources](https://biosustain.github.io/benchling-resources/guides/use_registry.html)

* [Register a strain collection in Benchling — Benchling resources](https://biosustain.github.io/benchling-resources/guides/strain_collection.html)


## The end of your Project

As you wrap up a specific study, or you reach the end of your stay at Biosustain, it’s important to consider the fate of the data you are leaving behind in Benchling. 

**First**, you must consider whether the data in the Projects you have worked on is complete:

* Does every entry have a clear purpose and conclusion?

    * Even if sub-projects were stopped, it is important to take note of this and state why.

* Have all relevant entities been registered?

    * Think of items you would like to leave behind and their locations: strains in -80C freezers, plasmids in -20C freezers. 

    * You may have sequence entities which do not have physical instances (eg. a plasmid that needs to be obtained via miniprep of a strain, or failed constructs). Make sure to clearly label them as such, and to link to other relevant entities when necessary. This may be useful for future users when using the global search and trying to locate sequences. 

* Is it easy to browse through my project folders?

    * Make sure your folder structure is well organized. You can always include a README entry to guide others through your folders. 

* Are there any findings that were not published, but would still be useful to others?

    * Negative results

    * Optimized protocols (eg. tricks to improve miniprep yield, how to increase transformation efficiency, or troubleshooting tips for different techniques)

**Then**, you must make sure people in your team will have access to your data. Share the folder with your team or copy the contents of the project into a folder of the shared team project. Note that the data moved to a new location will have the permission settings of the project folder it is moved into. 

**Lastly**, make sure you still have access to your data while wrapping up. If you're finishing a project at Biosustain but still need time to organize or finalize your work in Benchling, you should request temporary extended access through HR. Keep in mind that after your stay ends, access to the Biosustain Benchling tenant will no longer be available, unless otherwise arranged.

*With the previous tips in mind, your experience with the management of projects in Benchling should be as smooth as possible!*

````{admonition} ℹ️​ A note on data storage
:class: my-custom-admonition
You should also consider what to do with data stored elsewhere. 

It’s important to note that once your DTU account is suspended, its associated OneDrive account will also be. This means that data created or shared by you will be deleted, including shared OneDrive folders, if they are linked to your account. Thus, you must remember to save important data to the O drive, to ensure it will remain accessible to others (Department Drive-NNFCFB). Avoid leaving data behind in the M drive, which only you have access to. 

For other kinds of data management inquiries, you can always **[contact the RDM team](https://biosustain.github.io/benchling-resources/contact.html)** to ask questions.

````

<br/><br/>



If you have any question, don’t hesitate to contact us at [lims_support@biosustain.dtu.dk](mailto:lims_support@biosustain.dtu.dk).
