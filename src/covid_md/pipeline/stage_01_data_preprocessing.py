from covid_md import logger
from covid_md.components import DataPreprocessing
from covid_md.config import ConfigurationManager

STAGE_NAME= "DATA_PREPROCESSING"

def main():
    config= ConfigurationManager()
    data_preprocessing_config= config.data_preprocessing()
    data_preprocessing= DataPreprocessing(config= data_preprocessing_config)
    data_preprocessing.data_prep()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>Stage: {STAGE_NAME} is started<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>Stage: {STAGE_NAME} is completeded<<<<<<<<<<")
    except Exception as e:
        raise e