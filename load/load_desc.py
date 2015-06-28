import csv
import os
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor
from collections import defaultdict
from load.ttp import TermTypePair


class DescProcessor(BaseProcessor):

    def process(self):
        sc = SnomedConfig().ConfigSectionMap("FileSection")
        dir = os.path.dirname(os.path.dirname(__file__))
        print(dir)
        descFile = os.path.join(dir, sc["descfile"])
        data_dict = defaultdict(list)
        with open(descFile, "rt", encoding='utf-8') as tsvin:
            dictReader = csv.DictReader(
                tsvin, delimiter="\t", quoting=csv.QUOTE_NONE)
            # iterate and set the dict with all terms
            for v in dictReader:
                data_dict[v['conceptId']].append(TermTypePair(v['term'], v['typeId']))

        return data_dict
