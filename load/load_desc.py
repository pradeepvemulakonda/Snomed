import csv
import os
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor
from collections import defaultdict
from load.ttp import TermTypePair


class DescProcessor(BaseProcessor):

    def process(self):
        input_file = super().get_files('descfile')
        print(input_file)
        data_dict = defaultdict(list)
        with open(input_file[0], "rt", encoding='utf-8') as tsvin:
            dictReader = csv.DictReader(
                tsvin, delimiter="\t", quoting=csv.QUOTE_NONE)
            # iterate and set the dict with all terms
            for v in dictReader:
                data_dict[v['conceptId']].append(TermTypePair(v['term'],
                                                              v['typeId']))

        return data_dict
