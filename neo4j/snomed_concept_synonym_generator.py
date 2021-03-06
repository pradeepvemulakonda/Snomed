import csv
import os
from worker.abstract_item_generator import BaseItemGenerator

__author__ = 'pradeepv'


class SnomedConceptSynonymGenerator(BaseItemGenerator):

    def __init__(self):
        self.input_file = super().file_to_read('conceptfileadd')
        self.infile = None

    @property
    def generate(self):
        """Process the file."""
        print('reading files')
        self.infile = open(self.input_file, 'rt', encoding='utf-8')
        reader = csv.DictReader(self.infile, quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        return reader

    def close(self):
        self.infile.close()
