import os
import time
from config.read_config import SnomedConfig
from zip_processor.snomed_zip_processor import SnomedArchiveProcessor
from os import listdir
from os.path import isfile
from load.import_concepts import ConceptProcessor
from load.import_rel import RelationProcessor
from load.load_desc import DescProcessor
from neo4j.snomed_concept_processor import SnomedConceptProcessor
from neo4j.snomed_concept_generator import SnomedConceptGenerator
from neo4j.snomed_concept_synonym_generator import SnomedConceptSynonymGenerator
from neo4j.snomed_concept_synonym_processor import SnomedConceptSynonymProcessor
from neo4j.snomed_relation_generator import SnomedRelationGenerator
from neo4j.snomed_relation_processor import SnomedRelationProcessor
from worker.thread_executor import ThreadExecutor

__author__ = 'pradeepv'
print('starting processing snomed zip file ...')
start_time = time.time()
print('start time ' + time.ctime())
sc = SnomedConfig().ConfigSectionMap("FileSection")
zip_file_directory = sc["snomedziplocation"]
zip_file_name = listdir(zip_file_directory).pop()
zip_file = os.path.join(zip_file_directory,zip_file_name)

print('Found the zip file '+ zip_file +' and stating processing ...')

if isfile(zip_file):
    print(zip_file)
    sap = SnomedArchiveProcessor(zip_file)
    sap.process()
else:
    raise FileNotFoundError

print('Zip file is extracted into required files')
start_time_int = time.time()
# load the description file into a dict
ld = DescProcessor()
print("loading descriptions ...")
descMap = ld.process()

# pass the desc dict as an init param
cp = ConceptProcessor(descMap)
rp = RelationProcessor(descMap)

# process concept and rel
print("creating concepts csv ...")
cp.process()
print("creating relations csv ...")
rp.process()
print("--- total time taken to create intermediate files %s seconds ---" % (time.time() - start_time_int))

print("starting 5 threads to upload snomed concepts")
start_time_con = time.time()
cte = ThreadExecutor(20)
sg = SnomedConceptGenerator()
sp = SnomedConceptProcessor()
cte.execute(sg, sp)
print("upload of snomed concepts complete")
print("--- time taken to upload concepts %s seconds ---" % (time.time() - start_time_con))

print("starting 5 threads to upload snomed synonyms")
start_time_syn = time.time()
ste = ThreadExecutor(20)
sg = SnomedConceptSynonymGenerator()
sp = SnomedConceptSynonymProcessor()
ste.execute(sg, sp)
print("upload of snomed synonyms complete")
print("--- time taken to upload synonyms %s seconds ---" % (time.time() - start_time_syn))

print("upload snomed relationships started..")
print("Going to take approximately 1.5 hours... grab a coffee .. and relax")
start_time_rel = time.time()
rte = ThreadExecutor(1)
sg = SnomedRelationGenerator()
sp = SnomedRelationProcessor()
rte.execute(sg, sp)
print("upload of snomed relations complete")

print("--- time taken to upload relations %s seconds ---" % (time.time() - start_time_rel))

print("Completed upload of entire snomed snapshot details")
print("--- total time taken %s seconds ---" % (time.time() - start_time))

