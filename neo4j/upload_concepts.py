from neo4j.base_uploader import BaseUploader

__author__ = 'pradeepv'

class UploadConcept(BaseUploader):

    statement = "CREATE (c:Concept:FSA {conceptId: {id}, term: {term}, descType: {descType}});"

    create_index_concept_id = "CREATE INDEX ON :Concept(conceptId)"
    create_index_term = "CREATE INDEX ON :Concept(term)"

    def __init__(self, graph_url, file_to_process):
        super().__init__(graph_url, file_to_process)

    def setup(self, graph):
        tx = graph.begin()
        tx.run(UploadConcept.create_index_concept_id)
        tx.run(UploadConcept.create_index_term)
        tx.commit()

    def add_query(self, record, tx):
        tx.append(UploadConcept.statement, {"id": record["id"],
                                            "term": record["term"],
                                            "descType": record["descType"]})