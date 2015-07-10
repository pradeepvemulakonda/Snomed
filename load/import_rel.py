import csv
import os
import re
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor


class RelationProcessor(BaseProcessor):
    def __init__(self, descMap):
        self.descMap = descMap

    def process(self):
        rel_file, rel_out_file, rel_add_file = super().get_files('relfile')
        relSet = dict()
        with open(rel_file, 'rt', encoding='utf-8') as infile, \
                open(rel_out_file, 'wt', encoding='utf-8') as outfile, \
                open(rel_add_file, 'wt', encoding='utf-8') as addfile:
            reader = csv.DictReader(
                infile, delimiter="\t", quoting=csv.QUOTE_NONE)
            # Use the same field names for the output file.
            fieldnames = ['id', 'effectiveTime', 'active', 'moduleId',
                          'sourceId', 'destinationId', 'relationshipGroup',
                          'typeId', 'characteristicTypeId', 'modifierId',
                          'term', 'descType', 'relLabel']
            writer = csv.DictWriter(outfile, fieldnames)
            writer.writeheader()

            writerAdd = csv.DictWriter(addfile, fieldnames)
            writerAdd.writeheader()

            # Iterate over the products in the input.

            for rel in reader:
                result = self.descMap.get(rel['typeId'], [])
                for termType in result:
                    copiedRel = rel.copy()
                    # Update the product info.
                    copiedRel['term'] = termType.getTerm()
                    copiedRel['descType'] = termType.getTypeId()
                    if (copiedRel['typeId'] in relSet):
                        copiedRel['relLabel'] = relSet[copiedRel['typeId']]
                    else:
                        formattedTerm = re.sub(
                            r"\([^)]*\)|[^a-zA-Z0-9_\s]", "", termType.getTerm())
                        formatetdTerm = "_".join(
                            formattedTerm.upper().rstrip().split())
                        relSet[copiedRel['typeId']] = formatetdTerm
                        copiedRel['relLabel'] = formatetdTerm
                    # Write it to the output file.
                    # Write it to the output file.
                    if '900000000000003001' == termType.getTypeId():
                        writer.writerow(copiedRel)
                    else:
                        writerAdd.writerow(copiedRel)

