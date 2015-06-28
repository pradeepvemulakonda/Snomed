import csv
import os
import abc
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor

class DescProcessor(BaseProcessor):

    def process(self):
        sc = SnomedConfig().ConfigSectionMap("FileSection")
        dir = os.path.dirname(os.path.dirname(__file__))
        print(dir)
        descFile = os.path.join(dir, sc["descfile"])

        with open(descFile, "rt", encoding='utf-8') as tsvin, open("new.csv", "wb") as tsvout:
            dictReader = csv.DictReader(tsvin, delimiter="\t", quoting=csv.QUOTE_NONE)
            csv.writer(tsvout)

            desc_result = dict(
                (v['conceptId'], v['term']) for v in dictReader if v['typeId'] == "900000000000003001"
            )

        return desc_result