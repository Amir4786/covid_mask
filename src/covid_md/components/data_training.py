from covid_md import logger
from covid_md.entity import DataTrainingConfig
from covid_md.config import ConfigurationManager

from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten,Dropout
from keras.layers import Conv2D,MaxPooling2D
from keras.callbacks import ModelCheckpoint

import os
import numpy as np
from pathlib import Path

class DataTraining:
    def __init__(self,config: DataTrainingConfig):
        self.config= config
    def load_data(self):
        logger.info("loading array files...")
        os.chdir(self.config.data_path)
        data= np.load('data.npy')
        target= np.load('target.npy')
        os.chdir("../../")
        return data, target
    def training_skeleton(self,data):
        logger.info("giving CNN skeleton for training...")
        model= Sequential()

        model.add(Conv2D(200,(3,3),input_shape= data.shape[1:]))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        logger.info("The first CNN layer followed by Relu and MaxPooling layers")
        model.add(Conv2D(100,(3,3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        logger.info("The second convolution layer followed by Relu and MaxPooling layers")
        model.add(Flatten())
        model.add(Dropout(0.5))
        logger.info("Flatten layer to stack the output convolutions from second convolution layer")
        model.add(Dense(50, activation='relu'))
        logger.info("Dense layer of 64 neurons")
        model.add(Dense(2, activation= 'softmax'))
        logger.info("The Final layer with two outputs for two categories")
        model.compile(loss= 'categorical_crossentropy', optimizer= 'adam', metrics= ['accuracy'])
        return model
    def split_data(self, data, target):
        logger.info("split the data into train and test for features and target values...")
        test_size= self.config.test_size
        train_data,test_data,train_target,test_target= train_test_split(data,target, test_size= test_size)
        return train_data,test_data,train_target,test_target
    def checkpoint(self):
        logger.info("giving the checkpoint")
        model= self.config.model
        monitor= self.config.monitor
        verbose= self.config.verbose
        best_model= self.config.save_best_only
        mode= self.config.mode
        cp= ModelCheckpoint(model, monitor= monitor, verbose= verbose, save_best_only= best_model, mode= mode)
        return cp
    def final_training(self,train_data, train_target,checkpoint,model):
        logger.info("final training...")
        epochs= self.config.epochs
        validation_split= self.config.validation_split
        os.chdir(self.config.root_dir)
        history= model.fit(train_data, train_target, epochs= epochs, callbacks= [checkpoint], validation_split= validation_split)
        os.chdir("../../")
        return history