import configparser
import os

from Exceptions import ConfigFileNotExistError, OptionNotExistError


class ConfigsFromFile:
    __configs = configparser.ConfigParser()

    def read_configs(self, config_path):
        if os.path.isfile(config_path):
            self.__configs.read(config_path)
        else:
            raise ConfigFileNotExistError

    def get_value_with_existence_checking(self, section, option):
        if self.__configs.has_option(section, option):
            value = self.__configs[section][option]
        else:
            raise OptionNotExistError(section, option)

        return value

    def get_value_with_default_padding(self, section, option, default_value):
        if self.__configs.has_option(section, option):
            value = self.__configs[section][option]
        else:
            value = default_value

        return value
