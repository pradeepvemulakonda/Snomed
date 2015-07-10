import abc
import os
from config.read_config import SnomedConfig


class BaseProcessor(object):
    __metaclass__ = abc.ABCMeta

    sc = SnomedConfig().ConfigSectionMap("FileSection")
    dir = os.path.dirname(os.path.dirname(__file__))
    input_file_path = os.path.join(dir, sc["snomedfiles"])
    files = os.listdir(input_file_path)

    @abc.abstractmethod
    def process(self):
        """Process the file."""
        return

    def get_files(self, fileType):
        outDirectory = os.path.join(BaseProcessor.dir, BaseProcessor.sc["resultslocation"])
        file_type_pattern = BaseProcessor.sc[fileType]
        for fileName in BaseProcessor.files:
            if file_type_pattern in fileName:
                return os.path.join(BaseProcessor.input_file_path, fileName), os.path.join(outDirectory, file_type_pattern + '.csv'), \
                    os.path.join(outDirectory, file_type_pattern + '_add' + '.csv', )
