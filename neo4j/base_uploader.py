__author__ = 'pradeepv'

import abc
import os
import csv
from py2neo import Graph
from py2neo import watch


class BaseUploader(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, graph_url, file_to_process):
        #watch("httpstream")
        self.graph = Graph(graph_url)
        self.setup(self.graph)
        dir = os.path.dirname(os.path.dirname(__file__))
        self.input_file = os.path.join(dir, file_to_process)
        self.idx = 0
        print('connected to graph db at : ' + str(self.graph))

    @abc.abstractmethod
    def setup(self, graph):
        """Process the file.
        :rtype : None
        """

    @abc.abstractmethod
    def add_query(self, record, tx):
        """Process the file."""
        return

    def process(self):
        """Process the file."""
        print('start processing')
        with open(self.input_file, 'rt', encoding='utf-8') as infile:
            reader = csv.DictReader(infile, quoting=csv.QUOTE_NONE)
            tx = self.graph.begin()
            for row in reader:
                if self.idx % 1000 == 0 and self.idx != 0:
                    tx.commit()
                    tx = self.graph.begin()
                    print('commited 1000 rows till row:' + str(self.idx))
                self.add_query(row, tx)
                self.idx += 1
            tx.commit()
