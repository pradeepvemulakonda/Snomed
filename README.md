Snomed
======

Create a Neo4j database to import AMT/Snomed drug files and provide a REST interface to access the data

<h5>Prepare files to be uploaded to Neo4j</h5>

- update the config.ini file in the config folder to the paths in the snomed_files folder.
- Run the process_files.py
- the updated concepts and relationship files with the term and description type id is present in the results folder.

<h6>TODO</h6>
- Update the relationships file with RELATION_LABEL, i.e. a unique label with no spaces to identify the realtionship type.

<h5>Upload data to Neo4j</h5>
