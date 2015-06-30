import os
import csv
from py2neo import Graph
from string import Template
from py2neo import watch
from neo4j.base_uploader import BaseUploader


class UploadRelationships(BaseUploader):

    statement = Template("MATCH (source:Concept:FSA) WHERE source.conceptId = '$sourceId' " \
                         "MATCH (dest:Concept:FSA) WHERE dest.conceptId = '$destinationId' " \
                         "CREATE (source)-[r:$label{relId:'$typeId', term: '$term', descType: '$descType'}]->(dest)")

    def __init__(self, graph_url, file_to_process):
        super().__init__(graph_url, file_to_process)

    def setup(self, graph):
        pass

    def add_query(self, record, tx):
        local_statement = UploadRelationships.statement.substitute(sourceId=record['sourceId'],
                                                                   destinationId=record['destinationId'],
                                                                   label=record['relLabel'],
                                                                   typeId=record['typeId'],
                                                                   term=record['term'],
                                                                   descType=record['descType'])
        tx.append(local_statement)

