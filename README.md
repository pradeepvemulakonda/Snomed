Snomed
======

Create a Neo4j database to import Snomed drug files and provide a REST interface to access the data.

For information reg Neo4j please visist http://neo4j.com/

<h5>Prepare files to be uploaded to Neo4j</h5>

- update the config.ini file in the config folder as required.
- Run the run_snomed_upload.py
- the updated concepts and relationship files with the term and description type id is present in the results folder.
- the script uploads concepts, synonyms and relations into a neo4j instance.
- The graph database url should be specified in config.ini file.
- The entire script takes about ~ 2 hours to upload a snomed snapshot into a new neo4j database.

<h5>TODO</h5>
- DSL to query data from neo4j.(Scala)
- Faster upload(may be scala | Graphx)
- Update existing installation with delta
- UX to provide DSL queries.(Play framework)
- Provie scripts for AMT, RxNorm and DND.
- Sample Cypher queries.
- Better logging.
- Unit tests
- Rest Interface

