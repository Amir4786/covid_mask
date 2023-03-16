from covid_md import logger
from covid_md.components import MaskDetection
from covid_md.config import ConfigurationManager

STAGE_NAME= "FACE_MASK_DETECTION"

def main():
    logger.info("give details...")
    config= ConfigurationManager()
    logger.info("calling configuration setup...")
    mask_detection_config= config.get_mask_detection_config()
    logger.info("calling mak detection...")
    mask_detection= MaskDetection(config= mask_detection_config)
    logger.info("loading the model...")
    model= mask_detection.load_model()
    logger.info("assigning values...")
    face_classifier, source, labels_dict, color_dict= mask_detection.other_params()
    logger.info("mask detection started...")
    mask_detection.face_mask_detection(model, face_classifier, source, labels_dict, color_dict)

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>Stage: {STAGE_NAME} is started<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>Stage: {STAGE_NAME} is completeded<<<<<<<<<<")
    except Exception as e:
        raise e