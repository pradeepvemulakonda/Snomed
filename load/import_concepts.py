import csv
import os
import abc
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor

class ConceptProcessor(BaseProcessor):

    def __init__(self, descMap):
        self.descMap = descMap

    def process(self):
        sc = SnomedConfig().ConfigSectionMap("FileSection")
        dir = os.path.dirname(os.path.dirname(__file__))
        conceptFile = os.path.join(dir, sc["conceptfile"])
        conceptOutFile = os.path.join(dir, sc["outputconceptfile"])

        with open(conceptFile, 'rt', encoding='utf-8') as infile:
            with open(conceptOutFile, 'wt', encoding='utf-8') as outfile:
                reader = csv.DictReader(infile, delimiter="\t", quoting=csv.QUOTE_NONE)
                print(reader.fieldnames)
                # Use the same field names for the output file.
                fieldnames = ['id', 'effectiveTime', 'active', 'moduleId', 'definitionStatusId', 'term']
                writer = csv.DictWriter(outfile, fieldnames)
                writer.writeheader()

                # Iterate over the products in the input.

                for concept in reader:
                    result = self.descMap.get(concept['id'], " ")

                    # Update the product info.
                    concept['term'] = result

                    # Write it to the output file.
                    writer.writerow(concept)
