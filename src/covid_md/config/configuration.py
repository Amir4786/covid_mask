from covid_md.constant import *
from covid_md.entity import (DataPreprocessingConfig, DataTrainingConfig, MaskDetectionConfig)
from covid_md.utils import read_yaml, create_directories
from pathlib import Path
from covid_md import logger

class ConfigurationManager:
    def __init__(self, config_filepath= CONFIG_FILE_PATH, params_filepath= PARAMS_FILE_PATH):
        self.config= read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    def data_preprocessing(self)->DataPreprocessingConfig:
        logger.info("data processing configuration...")
        config= self.config.data_preprocessing
        create_directories([config.root_dir])
        data_preprocessing_config= DataPreprocessingConfig(
            root_dir= self.config.data_preprocessing.root_dir,
            data_path= self.config.data_preprocessing.data_path,
            preprocess_records= self.config.data_preprocessing.preprocess_records
        )
        return data_preprocessing_config
    def get_data_training_config(self)-> DataTrainingConfig:
        logger.info("data training configuration...")
        config= self.config.data_training
        params= self.params.training
        create_directories([config.root_dir])
        data_training_config= DataTrainingConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            test_size= params.test_size,
            monitor= params.monitor,
            verbose= params.verbose,
            save_best_only= params.save_best_only,
            mode= params.mode,
            epochs= params.epochs,
            validation_split= params.validation_split,
            model= params.model
        )
        return data_training_config
    
    def get_mask_detection_config(self)->MaskDetectionConfig:
        config= self.config.mask_detection
        create_directories([config.root_dir])
        mask_detection_config= MaskDetectionConfig(
            root_dir= config.root_dir,
            face_classifier= config.face_classifier
        )
        return mask_detection_config