from neo4j.snomed_concept_processor import SnomedConceptProcessor
from neo4j.snomed_concept_generator import SnomedConceptGenerator
from neo4j.snomed_concept_synonym_generator import SnomedConceptSynonymGenerator
from neo4j.snomed_concept_synonym_processor import SnomedConceptSynonymProcessor
from neo4j.snomed_relation_generator import SnomedRelationGenerator
from neo4j.snomed_relation_processor import SnomedRelationProcessor
from worker.scheduling_thread_executor import SchedulingThreadExecutor
from worker.thread_executor import ThreadExecutor

__author__ = 'pradeepv'

# te = ThreadExecutor()
# sg = SnomedConceptGenerator()
# sp = SnomedConceptProcessor()
#
# te.execute(sg, sp)

# te = ThreadExecutor()
# sg = SnomedConceptSynonymGenerator()
# sp = SnomedConceptSynonymProcessor()
# 
# te.execute(sg, sp)

# does not work as neo4j throws deadlock errors
# te = ThreadExecutor(10)
# sg = SnomedRelationGenerator()
# sp = SnomedRelationProcessor()

# ste = SchedulingThreadExecutor(6)
# sg = SnomedRelationGenerator()
# sp = SnomedRelationProcessor()


te.execute(sg, sp)