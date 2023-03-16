from covid_md import logger
from covid_md.components import DataTraining
from covid_md.config import ConfigurationManager

STAGE_NAME= "DATA_TRAINING"

def main():
    logger.info("assigned values from imported files.")
    config= ConfigurationManager()
    logger.info("giving paths...")
    data_training_config= config.get_data_training_config()
    data_training= DataTraining(config= data_training_config)
    logger.info("split features and target values...")
    data,target= data_training.load_data()
    logger.info("giving CNN skeleton...")
    model= data_training.training_skeleton(data)
    logger.info("divide train and test data...")
    train_data,test_data,train_target,test_target= data_training.split_data(data, target)
    checkpoint= data_training.checkpoint()
    logger.info("final training started...")
    data_training.final_training(train_data, train_target, checkpoint, model)
    logger.info("final training finally finished...")
    logger.info("your models are stored in artifacts/data_training path")

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>Stage: {STAGE_NAME} is started<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>Stage: {STAGE_NAME} is completeded<<<<<<<<<<")
    except Exception as e:
        raise e