from CoreConfig.ConfigDictionary import ConfigDictionary
from CoreConfig.ConfigsFromFile import ConfigsFromFile


class InitializeConfigDictionary:
    @staticmethod
    def execute(config_file_path):
        try:
            ConfigsFromFile().read_configs(config_file_path)
            ConfigDictionary().initialize_config_dict()
        except Exception:
            raise

    def ReadSystemwideConfig(config_file_path):
        try:
            ConfigsFromFile().read_common_configs(config_file_path)
            ConfigDictionary().add_systemwide_config_dict()
        except Exception:
            raise
