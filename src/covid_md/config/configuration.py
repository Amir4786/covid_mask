from covid_md.constant import *
from covid_md.entity import (DataPreprocessingConfig)
from covid_md.utils import read_yaml, create_directories
from pathlib import Path

class ConfigurationManager:
    def __init__(self, config_filepath= CONFIG_FILE_PATH, params_filepath= PARAMS_FILE_PATH):
        self.config= read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    def data_preprocessing(self)->DataPreprocessingConfig:
        config= self.config.data_preprocessing
        create_directories([config.root_dir])
        data_preprocessing_config= DataPreprocessingConfig(
            root_dir= self.config.data_preprocessing.root_dir,
            data_path= self.config.data_preprocessing.data_path,
            preprocess_records= self.config.data_preprocessing.preprocess_records
        )
        return data_preprocessing_config