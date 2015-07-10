import csv
import os
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor


class ConceptProcessor(BaseProcessor):
    def __init__(self, descMap):
        self.descMap = descMap

    def process(self):
        concept_file, concept_out_file, concept_add_file = super().get_files('conceptfile')

        with open(concept_file, 'rt', encoding='utf-8') as infile, \
                open(concept_out_file, 'wt', encoding='utf-8') as outfile, \
                open(concept_add_file, 'wt', encoding='utf-8') as addfile:
            reader = csv.DictReader(
                infile, delimiter="\t", quoting=csv.QUOTE_NONE)
            print(reader.fieldnames)
            # Use the same field names for the output file.
            fieldnames = ['id', 'effectiveTime', 'active',
                          'moduleId', 'definitionStatusId', 'term',
                          'descType']
            writer = csv.DictWriter(outfile, fieldnames)
            writer.writeheader()

            writerAdd = csv.DictWriter(addfile, fieldnames)
            writerAdd.writeheader()

            # Iterate over the products in the input.

            for concept in reader:
                result = self.descMap.get(concept['id'], [])
                for termType in result:
                    copiedConcept = concept.copy()
                    # Update the product info.
                    copiedConcept['term'] = termType.getTerm()
                    copiedConcept['descType'] = termType.getTypeId()
                    # Write it to the output file.
                    if '900000000000003001' == termType.getTypeId():
                        writer.writerow(copiedConcept)
                    else:
                        writerAdd.writerow(copiedConcept)
