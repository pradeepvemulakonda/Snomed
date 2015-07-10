from py2neo.core import Graph
from py2neo import watch
from worker.abstract_item_processor import BaseItemProcessor

__author__ = 'pradeepv'


class SnomedConceptSynonymProcessor(BaseItemProcessor):
    statement = "MATCH (dest:Concept:FSA) WHERE dest.conceptId = {id} " \
                "CREATE (c:Concept:Synonym{conceptId: {id}, term: {term}," \
                " descType: {descType}})-[r:IS_A { relId: '116680003'," \
                " term: 'Is a (attribute)', descType: '900000000000003001'}]->(dest);"

    def __init__(self):
        watch("httpstream")
        self.graph = Graph(super().graph_url)

    def process(self, record, tx):
        tx.append(SnomedConceptSynonymProcessor.statement, {"id": record["id"],
                                                            "term": record["term"],
                                                            "descType": record["descType"]})
