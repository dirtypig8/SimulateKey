from CoreConfig.ConfigsFromFile import *
from CoreConfig.DefaultValues import *


class ConfigDictionary:
    config_dict = dict()

    @staticmethod
    def initialize_config_dict():
        try:
            ConfigDictionary.config_dict = {
                "equip_id": ConfigsFromFile().get_value_with_existence_checking("System", "equip_id"),                
                "shop_id": ConfigsFromFile().get_value_with_existence_checking("System", "shop_id"),
                "lot_id": ConfigsFromFile().get_value_with_existence_checking("System", "lot_id"),                
                "log_path": ConfigsFromFile().get_value_with_default_padding(
                    "System", "log_path", DefaultLogPathGetter().execute()
                ),
                "static_data_dir_path": ConfigsFromFile().get_value_with_default_padding(
                    "System", "static_data_dir_path", DefaultStaticDataDirPathGetter().execute()
                ),
                "lot_name": ConfigsFromFile().get_value_with_existence_checking("System", "lot_name"),
                "shop_name": ConfigsFromFile().get_value_with_existence_checking("System", "shop_name"),
                "name_color": ConfigsFromFile().get_value_with_existence_checking("System", "name_color"),
                "password": ConfigsFromFile().get_value_with_existence_checking("System", "password"),
                "api_key": ConfigsFromFile().get_value_with_existence_checking("System", "api_key"),
                "qr_format": ConfigsFromFile().get_value_with_existence_checking("System", "qr_format"),
                
                "printer_version": ConfigsFromFile().get_value_with_existence_checking("Printer", "printer_version"),
                "thermal_printer": {
                    "host": ConfigsFromFile().get_value_with_existence_checking("Printer", "host"),
                    "port": int(ConfigsFromFile().get_value_with_existence_checking("Printer", "port")),
                },
            }

        except Exception:
            raise
