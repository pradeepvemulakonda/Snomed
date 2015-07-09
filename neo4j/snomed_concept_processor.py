from py2neo.core import Graph
from py2neo import watch
from worker.abstract_item_processor import BaseItemProcessor

__author__ = 'pradeepv'

class SnomedConceptProcessor(BaseItemProcessor):

    statement = "CREATE (c:Concept:FSA {conceptId: {id}, term: {term}, descType: {descType}});"
    graph_url = 'http://localhost:7474/db/data/'
    create_index_concept_id = "CREATE INDEX ON :Concept(conceptId)"
    create_index_term = "CREATE INDEX ON :Concept(term)"

    def __init__(self):
        watch("httpstream")
        self.graph = Graph(SnomedConceptProcessor.graph_url)
        tx = self.graph.cypher.begin()
        tx.append(SnomedConceptProcessor.create_index_concept_id)
        tx.append(SnomedConceptProcessor.create_index_term)
        tx.commit()

    def process(self, record, tx):
        tx.append(SnomedConceptProcessor.statement, {"id": record["id"],
                                            "term": record["term"],
                                            "descType": record["descType"]})
