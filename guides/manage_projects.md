# Project folder lifecycle in Benchling: How to keep research data structured and accessible

## Introduction 

**Project folders** (referred to as *projects* in this guide) are key elements of data management in Benchling. In these folders you can store notebook entries, protocols, and entities such as plasmids, oligos, and DNA sequences. You can also manage the access of your organization’s and your team’s users to your data. This article outlines good practices to keep in mind regarding the management of projects, to ensure that your data can be used to the fullest both during and after your stay at DTU Biosustian. 

```{figure} ../_static/images/projects1-project-structure.png
:width: 60%
:align: center
*Example of the structure of a **Project folder***

```

## The start of a project

All users can create projects in Benchling. The decision to create one can be made based on the established organization strategy specific to your team: some teams create one project folder per team member, while others opt for one project per ongoing study. Make sure to ask your team lead or supervisor!

Regardless of the organization strategy, the first thing to consider when creating a new project folder is who has access to it. Through the **Manage access** menu, you can define which users or teams can have access to your information, and what level of access each should have. 

````{dropdown}  Levels of access to a project folder
The actions users with different levels of permissions can take are outlined below:
```{figure} ../_static/images/projects6-permissions.png
:width: 80%
:align: center

```
*Note: Users with append permission may be able to create blank entries, but they will then not be able to edit them. This permission may only be useful to append already completed documents and entities that do not require further editing by the user with this level of permission.*

````

```{figure} ../_static/images/projects2-manage-access.png
:width: 80%
:align: center
*View of the Manage Access menu*

```

`````{dropdown}  Bonus: Admin access policies

You can also specify separate levels of access for **users** and **admins** of a team. This may be useful if you would like to ensure a link between your project and your team, but you can’t share the data with the entire team yet. 

To do this, locate the team you want to manage the permissions of in the **Manage access** menu of your project, and follow these steps:

*More options button (…) > Add admin member access policy > Select level of access for users and admins*


```{figure} ../_static/images/projects3-admin-policy.png
:width: 80%
:align: center

*Setting an admin member access policy*

```
`````

### Recommendations

* When setting up a new project folder in Benchling, it is generally a good idea to organize your data by **research project** rather than by user. This helps ensure that:

    * All collaborators have centralized access to the same data

    * Redundancy and data scattering across personal folders is avoided

* Whenever possible, add your team to the projects you create. This is useful for both team admins and users to keep track of projects in Benchling. 

    * You can easily view the projects that have been shared with your team through different menus, as shown below. 

```{figure} ../_static/images/projects4-shared-projects-overview.png
:width: 80%
:align: center

*Different ways of having an overview of the projects shared with your team*

```

* Try to create new project folders only when truly necessary, for example, when starting a research project with a new, specific set of collaborators, or when starting work completely unrelated to your existing projects. This can make using the global search easier to find sequences, protocols and notebook entries, as you can filter both by project folder and by subfolders. It also makes it easier to keep track of the permissions you have set. 

    * If you need to do tests to understand Benchling functionalities, you can use the [Biosustain Training](https://biosustain.benchling.com/biosustain/f_/xmPebKow-biosustain-training/?filter=section%3Aall%3Bfolder%3Alib_xmPebKow%3Btypes%3AIS_ONE_OF%3Afolder%2Centry%2Cprocess%2Cprotocol%2Cbulk_assembly%2Cbasic_folder_item%2Cprotein%2Cmixture%2Csequence%2Crna_sequence%2Coligo%2Crna_oligo%2Canalysis%2Cdataset%3BarchivePurposes%3AIS_ONE_OF%3ANOT_ARCHIVED%3BisAssociatedWithUnsubmittedRequestV2Submission%3AIS_FALSE%3BProcessesIsSystemDataFilter%3AIS_FALSE&offset=0&limit=50&sorts=starred%3A0%3Bname%3A0&q=&v=2) project folder for this purpose. 

````{admonition} ℹ️​ Sharing samples with Analytics
:class: my-custom-admonition

When submitting samples for the Analytics team, it is necessary to grant them write permission to your folder. Many users choose to create dedicated projects for this. 

We recommend creating a **single, team-wide folder** to create samples for analysis. 

````
````{admonition} ℹ️​ Make collaboration easier with a shared Team project
:class: my-custom-admonition

Having a ***shared team project folder*** can ease the process of sharing protocols, sequences, strain information, and experiment results.

Adding an entire team to a project ensures that new people who arrive will easily gain access to the data after they are added to the team in Benchling. 

```{figure} ../_static/images/projects5-team-project.png
:width: 80%
:align: center

*An example of a shared team project folder*

```


````

## Your project in use

The inner structure of your project folder may vary depending on your own needs, and you can create subfolders to furhter organize your data. Throughout your stay at Biosustain, it is good to keep in mind the purpose of the information you generate and store within Benchling, and how you (and others) will need it in the short, medium and long term. With this in mind, this section covers some suggestions for your day-to-day use of projects in Benchling.

<div class="admonition my-custom-admonition">
  <p class="admonition-title">ℹ️ Tip</p>
  <p>Some questions to guide you through the process of <strong>organizing your data</strong> (both within and outside of Benchling) are:</p>
  <ul style="margin-top: 0.4em; margin-bottom: 0.5em; padding-left: 2em; list-style-type: disc; font-size: 0.9em;">
    <li style="margin-bottom: 0.2em;">If external collaborators ask for some data after one year of running an experiment, can I find it easily?</li>
    <li style="margin-bottom: 0.2em;">Can my colleagues understand my experiments and find their results?</li>
    <li style="margin-bottom: 0.2em;">Is there an easy way to find items like strains or plasmids in the freezers?</li>
    <li style="margin-bottom: 0.2em;">Can I know if someone has a plasmid I need without asking everyone?</li>
    <li style="margin-bottom: 0.2em;">If I left right now, could people know where I left off and continue my work easily?</li>
  </ul>
</div>

### Requests for access

You may receive emails requesting access to your project folder. The format of these emails is the following:

*"**[User]** has requested to be added to **[Project folder]**, so that they can access **[Entry or entity]**. To grant access, add them as a collaborator on the project, add them to a team that already has access, or move the item to a project that they already have access to."*

As the message states, if it is a user that should be on your team, ask a team admin to add them via the **Team** page. If that is not the case, you can grant them individual permission through the **Manage access** menu. You can also copy the contents the user is requesting to see into a project where they already have access. 

### Browsing projects

There are two main ways to browse through Benchling entries and entities:

* Within a project, you can use the search bar to find contents, including items in subfolders. 

```{figure} ../_static/images/projects7-browse-projects.gif
:width: 80%
:align: center

```

* Through the global search, you can browse through all data types in Benchling across all projects you have access to. 

    * With the global search, you can set the serach, type and add relevant filters first and then click through projects you have access to.

    * Using filters to your advantage, you can quickly locate entries, such as protocols created within your folder or your team’s shared folder.

```{figure} ../_static/images/projects8-global-search.gif
:width: 80%
:align: center

```

**Saved searches** can come in quite handy when you need to apply a lot of filters. You can also link to saved searches directly in your ELN entries so you can find relevant entities without leaving your notebook. 

### Using attachments to your advantage

You can attach files to your ELN, with a limit per attachment of 2 GB. While these files are not findable in Benchling through the global search, it may be useful to keep track of which files were generated in a given day, or as an additional backup for relevant data. It can also help you access things like protocols more quickly, as you can use the *“Open preview”* button to view attachments. 

```{figure} ../_static/images/projects9-attachments.gif
:width: 80%
:align: center

```

### Maintaining collections

While you may create and store plasmid, strain and primer collections externally (for example, in a spreadsheet shared through OneDrive), it is recommended to periodically update them to the Benchling Registry. 

You may find the following guides helpful for this purpose:

* [Understand the Registry — Benchling resources](https://biosustain.github.io/benchling-resources/guides/use_registry.html)

* [Register a strain collection in Benchling — Benchling resources](https://biosustain.github.io/benchling-resources/guides/strain_collection.html)


## The end of a project

As you wrap up a specific study, or you reach the end of your stay at Biosustain, it’s important to consider the fate of the data you are leaving behind in Benchling. 

````{admonition} ℹ️​ A note on data storage
:class: my-custom-admonition
You should also consider what to do with data stored elsewhere. 

It’s important to note that once your DTU account is suspended, its associated OneDrive account will also be. This means that data created or shared by you will be deleted, including shared OneDrive folders, if they are linked to your account. Thus, you must remember to save important data to the O drive, to ensure it will remain accessible to others (Department Drive-NNFCFB). Avoid leaving data behind in the M drive, which only you have access to. 

For other kinds of data management inquiries, you can always **[contact the RDM team](https://biosustain.github.io/benchling-resources/contact.html)** to ask questions.

````

**First**, you must consider whether the data in the projects you have worked on is complete:

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