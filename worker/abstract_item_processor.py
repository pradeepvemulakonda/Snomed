from config.read_config import SnomedConfig

__author__ = 'pradeepv'

import abc


class BaseItemProcessor(object):
    __metaclass__ = abc.ABCMeta

    graph_url = SnomedConfig().ConfigSectionMap("FileSection")["graphurl"]

    @abc.abstractmethod
    def process(self):
        """Process the file.
        :rtype : None
        """
        return
