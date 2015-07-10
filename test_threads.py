from neo4j.snomed_concept_processor import SnomedConceptProcessor
from neo4j.snomed_concept_generator import SnomedConceptGenerator
from neo4j.snomed_concept_synonym_generator import SnomedConceptSynonymGenerator
from neo4j.snomed_concept_synonym_processor import SnomedConceptSynonymProcessor
from neo4j.snomed_relation_generator import SnomedRelationGenerator
from neo4j.snomed_relation_processor import SnomedRelationProcessor
from worker.scheduling_thread_executor import SchedulingThreadExecutor
from worker.thread_executor import ThreadExecutor

__author__ = 'pradeepv'

cte = ThreadExecutor(5)
sg = SnomedConceptGenerator()
sp = SnomedConceptProcessor()

cte.execute(sg, sp)

ste = ThreadExecutor(5)
sg = SnomedConceptSynonymGenerator()
sp = SnomedConceptSynonymProcessor()

ste.execute(sg, sp)

rte = ThreadExecutor(1)
sg = SnomedRelationGenerator()
sp = SnomedRelationProcessor()

rte.execute(sg, sp)