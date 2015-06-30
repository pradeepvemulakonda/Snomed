import configparser
import os

class SnomedConfig:
    Config = configparser.ConfigParser()
    Config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

    def ConfigSectionMap(self, section):
        """
    
            :rtype : _ast.Dict
            """
        configMap = {}
        options = self.Config.options(section)
        for option in options:
            try:
                configMap[option] = self.Config.get(section, option)
                if configMap[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                configMap[option] = None
        return configMap

