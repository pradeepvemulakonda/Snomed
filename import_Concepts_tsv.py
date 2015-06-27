from config.read_config import SnomedConfig
import csv
import os

sc = SnomedConfig().ConfigSectionMap("FileSection")
dir = os.path.dirname(__file__)
descFile = os.path.join(dir, sc["descfile"])
conceptFile = os.path.join(dir, sc["conceptfile"])

with open(descFile, "rt", encoding='utf-8') as tsvin, open("new.csv", "wb") as tsvout:
    dictReader = csv.DictReader(tsvin, delimiter="\t")
    csv.writer(tsvout)

    desc_result = dict(
        (v['conceptId'], v['term']) for v in dictReader
    )


with open(conceptFile, 'rt', encoding='utf-8') as infile:
    with open('conceptOutFile.csv', 'wt', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, delimiter="\t")
        print(reader.fieldnames)
        # Use the same field names for the output file.
        fieldnames = ['id', 'effectiveTime', 'active', 'moduleId', 'definitionStatusId', 'term']
        writer = csv.DictWriter(outfile, fieldnames)
        writer.writeheader()

        # Iterate over the products in the input.

        for concept in reader:
            print(concept)
            result = desc_result.get(concept['id'], " ")

            # Update the product info.
            concept['term'] = result

            # Write it to the output file.
            writer.writerow(concept)
