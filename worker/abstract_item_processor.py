__author__ = 'pradeepv'

import abc


class BaseItemProcessor(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def process(self):
        """Process the file.
        :rtype : None
        """
        return
