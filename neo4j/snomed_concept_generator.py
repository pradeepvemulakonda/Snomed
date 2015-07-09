import csv
import os
from worker.abstract_item_generator import BaseItemGenerator

__author__ = 'pradeepv'


class SnomedConceptGenerator(BaseItemGenerator):
    file_to_process = 'results/processed_concept.csv'

    def __init__(self):
        dir = os.path.dirname(os.path.dirname(__file__))
        self.input_file = os.path.join(dir, SnomedConceptGenerator.file_to_process)
        self.infile = None

    @property
    def generate(self):
        """Process the file."""
        print('reading files')
        self.infile = open(self.input_file, 'rt', encoding='utf-8')
        reader = csv.DictReader(self.infile, quoting=csv.QUOTE_NONE)
        return reader

    def close(self):
        self.infile.close()
