from CoreConfig.ConfigDictionary import ConfigDictionary
import os


class ResourceGetter:
    @staticmethod
    def get_resource(*args):
        static_data_dir_path = ConfigDictionary.config_dict["static_data_dir_path"]
        file_path = os.path.join(static_data_dir_path, *args)
        qt_file_path = file_path.replace("\\", "/")
        return qt_file_path
