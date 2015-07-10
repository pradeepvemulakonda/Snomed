from py2neo.core import Graph
from py2neo import watch
from worker.abstract_item_processor import BaseItemProcessor
from string import Template

__author__ = 'pradeepv'


class SnomedRelationProcessor(BaseItemProcessor):
    statement = Template("MATCH (source:Concept:FSA) WHERE source.conceptId = '$sourceId' " \
                         "MATCH (dest:Concept:FSA) WHERE dest.conceptId = '$destinationId' " \
                         "CREATE (source)-[r:$label{relId:'$typeId', term: '$term', descType: '$descType'}]->(dest)")


    def __init__(self):
        watch("httpstream")
        self.graph = Graph(super().graph_url)


    def process(self, record, tx):
        local_statement = SnomedRelationProcessor.statement.substitute(sourceId=record['sourceId'],
                                                                   destinationId=record['destinationId'],
                                                                   label=record['relLabel'],
                                                                   typeId=record['typeId'],
                                                                   term=record['term'],
                                                                   descType=record['descType'])
        tx.append(local_statement)
