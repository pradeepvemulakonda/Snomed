Snomed - Python 
> For a Groovy version => https://github.com/pradeepvemulakonda/snomed-groovy

> Wiki => 
> https://github.com/pradeepvemulakonda/Snomed/wiki

<strong>Environment:</strong> mac(any linux or windows env) with <strong>python 3.6.1 and py2neo 3.1.2</strong>. Use a virtual environment to avoid any conflicts or errors.

CreateCreate a Neo4j database to import Snomed drug files and provide a REST interface to access the data.

For information reg Neo4j please visit http://neo4j.com/

Application is written in python and accepts a Snomed-CT zip file. The data from Snomed-CT around 3 miliion rows of TDV files will be uploaded to the graph database Neo4j.

Neo4j is a NoSql graph database which has a rich query capabilities which makes it ideal for decesion support and BI.

<h5>Prepare files to be uploaded to Neo4j</h5>

- Use Neo4j version 3.2.1
- update the config.ini file in the config folder as required. Only update the zip folder path.
- Run the run_snomed_upload.py
- the updated concepts and relationship files with the term and description type id is present in the results folder.
- the script uploads concepts, synonyms and relations into a neo4j instance.
- The graph database url should be specified in config.ini file.
- The entire script takes about ~ 2 hours to upload a snomed snapshot into a new neo4j database.
- Update of the Snomed Concepts is done using threads.
- Update of Relationships is done using a single thread as Neo4j is throwing deadlock exceptions if we process the relations in parallel.

