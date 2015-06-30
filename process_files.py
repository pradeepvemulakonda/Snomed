from load.import_concepts import ConceptProcessor
from load.import_rel import RelationProcessor
from load.load_desc import DescProcessor

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