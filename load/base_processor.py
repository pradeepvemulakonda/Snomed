import abc

class BaseProcessor(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def process(self):
        """Process the file."""
        return