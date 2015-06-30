from neo4j.base_uploader import BaseUploader

__author__ = 'pradeepv'

class UploadSynConcept(BaseUploader):

    statement = "MATCH (dest:Concept:FSA) WHERE dest.conceptId = {id} " \
                "CREATE (c:Concept:Synonym{conceptId: {id}, term: {term}," \
                " descType: {descType}})-[r:IS_A { relId: '116680003'," \
                " term: 'Is a (attribute)', descType: '900000000000003001'}]->(dest);"

    create_index_concept_id = "CREATE INDEX ON :Concept(conceptId)"
    create_index_term = "CREATE INDEX ON :Concept(term)"

    def __init__(self, graph_url, file_to_process):
        super().__init__(graph_url, file_to_process)

    def setup(self, graph):
        pass

    def add_query(self, record, tx):
        tx.append(UploadSynConcept.statement, {"id": record["id"],
                                            "term": record["term"],
                                            "descType": record["descType"]})