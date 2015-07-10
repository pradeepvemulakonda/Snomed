import os
from config.read_config import SnomedConfig

__author__ = 'pradeepv'

import abc

class BaseItemGenerator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate(self):
        """Process the file.
        :rtype : None
        """
        return

    def file_to_read(self, file_type):
        sc = SnomedConfig().ConfigSectionMap("FileSection")
        file_pattern_resolved = sc[file_type]
        dir = os.path.dirname(os.path.dirname(__file__))
        input_file_path = os.path.join(dir, sc["resultslocation"])
        files = os.listdir(input_file_path)
        for fileName in files:
            if file_pattern_resolved in fileName:
                return os.path.join(input_file_path, fileName)