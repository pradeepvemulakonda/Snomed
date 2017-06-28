import abc
import os
from config.read_config import SnomedConfig


class BaseProcessor(object):
    __metaclass__ = abc.ABCMeta

    sc = SnomedConfig().ConfigSectionMap("FileSection")
    dir = os.path.dirname(os.path.dirname(__file__))
    input_file_path = os.path.join(dir, sc["snomedfiles"])
    files = None

    @abc.abstractmethod
    def process(self):
        """Process the file."""
        return

    def get_files(self, fileType):
        self.files = os.listdir(self.input_file_path)
        outDirectory = os.path.join(BaseProcessor.dir, BaseProcessor.sc["resultslocation"])
        print(outDirectory)
        file_type_pattern = BaseProcessor.sc[fileType]
        print(file_type_pattern)
        for fileName in self.files:
            if file_type_pattern in fileName:
                return os.path.join(BaseProcessor.input_file_path, fileName), os.path.join(outDirectory, file_type_pattern + '.csv'), \
                    os.path.join(outDirectory, file_type_pattern + '_add' + '.csv', )
