# Benchling terminology

Important Benchling terms and what they refer to:

| Term | Description |
| ---- | ----------- |
| Entity | Structured data object. There are default Benchling entities (e.g. DNA Sequence, Amino Acid Sequence, Oligo) and a Custom Entities. See full list of entities in table bellow. Entities can be created and stored within Projects, formally registered in the Registry or assigned Inventory locations. |
| Entry | Notebook page for research documentation. Can contain text, tables, images and links to Benchling entities. |
| Schema | Defined data structure of Entities, Entries, Workflows, Requests or Automation runs. A schema comprises a set of fields (of specific data types) that captures relevant properties of an object, including tracking its relationships with other objects within Benchling. |
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