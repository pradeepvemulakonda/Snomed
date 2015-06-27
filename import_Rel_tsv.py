from config.read_config import SnomedConfig
import csv
import os

sc = SnomedConfig().ConfigSectionMap("FileSection")
dir = os.path.dirname(__file__)
descFile = os.path.join(dir, sc["descfile"])
conceptFile = os.path.join(dir, sc["conceptfile"])
relFile = os.path.join(dir, sc["relfile"])

with open(descFile, "rt", encoding='utf-8') as tsvin, open("new.csv", "wb") as tsvout:
    dictReader = csv.DictReader(tsvin, delimiter="\t")
    csv.writer(tsvout)

    desc_result = dict(
        (v['conceptId'], v['term']) for v in dictReader
    )


with open(relFile, 'rt', encoding='utf-8') as infile:
    with open('relOutFile.csv', 'wt', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, delimiter="\t")
        print(reader.fieldnames)
        # Use the same field names for the output file.
        fieldnames = ['id', 'effectiveTime', 'active', 'moduleId', 'sourceId', 'destinationId', 'relationshipGroup', 'typeId', 'characteristicTypeId', 'modifierId', 'term']
        writer = csv.DictWriter(outfile, fieldnames)
        writer.writeheader()

        # Iterate over the products in the input.

        for rel in reader:
            print(rel)
            result = desc_result.get(rel['typeId'], " ")

            # Update the product info.
            rel['term'] = result

            # Write it to the output file.
            writer.writerow(rel)
