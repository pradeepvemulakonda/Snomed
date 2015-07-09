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