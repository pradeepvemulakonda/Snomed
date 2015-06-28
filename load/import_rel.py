import csv
import os
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor


class RelationProcessor(BaseProcessor):

    def __init__(self, descMap):
        self.descMap = descMap

    def process(self):
        sc = SnomedConfig().ConfigSectionMap("FileSection")
        dir = os.path.dirname(os.path.dirname(__file__))
        relFile = os.path.join(dir, sc["relfile"])
        relOutFile = os.path.join(dir, sc["outputrelfile"])

        with open(relFile, 'rt', encoding='utf-8') as infile:
            with open(relOutFile, 'wt', encoding='utf-8') as outfile:
                reader = csv.DictReader(
                            infile, delimiter="\t", quoting=csv.QUOTE_NONE)
                print(reader.fieldnames)
                # Use the same field names for the output file.
                fieldnames = ['id', 'effectiveTime', 'active', 'moduleId',
                              'sourceId', 'destinationId', 'relationshipGroup',
                              'typeId', 'characteristicTypeId', 'modifierId',
                              'term', 'descType']
                writer = csv.DictWriter(outfile, fieldnames)
                writer.writeheader()

                # Iterate over the products in the input.

                for rel in reader:
                    result = self.descMap.get(rel['typeId'], [])
                    for termType in result:
                        copiedRel = rel.copy()
                        # Update the product info.
                        copiedRel['term'] = termType.getTerm()
                        copiedRel['descType'] = termType.getTypeId()

                        # Write it to the output file.
                        writer.writerow(copiedRel)
