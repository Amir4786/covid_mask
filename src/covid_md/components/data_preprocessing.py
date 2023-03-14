from covid_md import logger
from covid_md.entity import DataPreprocessingConfig
from covid_md.config import ConfigurationManager
import os, cv2
import numpy as np
from keras.utils import np_utils


class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config= config
    logger.info("Let's prepare the data for training...")
    def data_prep(self):
        img_size= 100
        data= []
        target= []
        logger.info("From ConfigurationManager calling paths of required directories...")
        path= self.config.data_path
        categories= os.listdir(path)
        labels= [i for i in range(len(categories))]
        labels_dict= dict(zip(categories, labels))
        for category in categories:
            folder_path= os.path.join(self.config.data_path, category)
            img_names= os.listdir(folder_path)
            for img_name in img_names:
                img_path= os.path.join(folder_path, img_name)
                img= cv2.imread(img_path)
                try:
                    logger.info("Let's change color imae into gray scale image...")
                    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    logger.info("resize the image into 100x100")
                    resized= cv2.resize(gray,(img_size,img_size))
                    data.append(resized)
                    target.append(labels_dict[category])
                except Exception as e:
                    raise e
        logger.info("Again change the directory for saving the results...")
        os.chdir(self.config.preprocess_records)
        data= np.array(data)/255
        data= np.reshape(data,(data.shape[0],img_size,img_size,1))
        target= np.array(target)
        new_target= np_utils.to_categorical(target)
        logger.info("saving in numpy array format for fat training...")
        np.save('data', data)
        np.save('target',new_target)