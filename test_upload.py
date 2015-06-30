from neo4j.upload_concepts import UploadConcept
from neo4j.upload_relationships import UploadRelationships
from neo4j.upload_syn_concepts import UploadSynConcept

__author__ = 'pradeepv'

uploadConcept = UploadConcept('http://localhost:7474/db/data/', 'results/processed_concept.csv')
uploadConcept.process()

uploadSyn = UploadSynConcept('http://localhost:7474/db/data/', 'results/processed_add_concept.csv')
uploadSyn.process()

uploadSyn = UploadRelationships('http://localhost:7474/db/data/', 'results/processed_rel.csv')
uploadSyn.process()